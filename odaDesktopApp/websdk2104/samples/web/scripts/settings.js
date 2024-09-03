'use strict';

// Set client auth mode - true to enable client auth, false to disable it
var isClientAuthEnabled = false;
var linkViewTarget = '_blank'
var _delegateObject = {
    beforeDisplay(message) {

    	if (message.messagePayload.type == 'text' && message.messagePayload.actions.length == 3 && message.messagePayload.actions[0].postback.target == 'SystemIntentsRoutingAction.cancel'){

    		//remove last button
    		message.messagePayload.actions.pop();

    	}
        console.log('beforeDisplay: ' + JSON.stringify(message));

        /*
         * Handle custom channel extensions
         */
        if (message.messagePayload.type == 'text' && message.messagePayload.channelExtensions && message.messagePayload.channelExtensions.alert) {
            //print the message
            alert(message.messagePayload.channelExtensions.alert);
        }

        /*
         * User session time-out reminder
         */

        resetTimer();  //all messages reset the timer

        if (message.messagePayload.channelExtensions) {
          if (message.messagePayload.channelExtensions.lastState) {
            //ONLY RESPONSES WITH A LAST STATE PROPERTY SET THE TIMER
            setTimer(message.messagePayload.channelExtensions.lastState,
            message.messagePayload.channelExtensions.botId,
            message.messagePayload.channelExtensions.goToState);
          }
        }

        /*
         * split long text messages
         */

        if (message.messagePayload.type == 'text') {
            message.messagePayload.text = splitParagraph(message.messagePayload.text);
        }

        /*
         * Handling System.Webview component.
         * 1. webview components are rendered as cards layout with single card
         * 2. url contains ODA host URL and /webviews/
         */
        if (message.messagePayload.cards) {

            //cards must have at least a single action. So its save to access the
            //first card directly
            if (message.messagePayload.cards[0].actions[0].url.includes('/connectors/v2/webviews/')) {
                //change type "url" to type "webview". This then renders the webview in the
                //messenger's iFrame, not relying on "linkHandler" property to point to the
                //embedded iFrame
                message.messagePayload.cards[0].actions[0].type = "webview";
            }
        }
        return message;
    },
    beforeSend(message) {
        return message;
    },
    beforePostbackSend(postback) {
        return postback;
    }
}

/**
 * Initializes the SDK and sets a global field with passed name for it the can
 * be referred later
 *
 * @param {string} name Name by which the chat widget should be referred
 */
function initSdk(name) {
    // Retry initialization later if WebSDK is not available yet
    if (!WebSDK) {
        setTimeout(function () {
            initSdk(name);
        }, 2000);
        return;
    }

    if (!name) {
        name = 'Bots';          // Set default reference name to 'Bots'
    }
    var Bots;

    setTimeout(function () {
        /**
         * SDK configuration settings
         * Other than URI, all fields are optional with two exceptions for auth modes
         * In client auth disabled mode, 'channelId' must be passed, 'userId' is optional
         * In client auth enabled mode, 'clientAuthEnabled: true' must be passed             initUserHiddenMessage: 'show demo menu',
         */
        var chatWidgetSettings = {
            URI: getUri(),                               // ODA URI, only the hostname part should be passed, without the https://
            clientAuthEnabled: isClientAuthEnabled,     // Enables client auth enabled mode of connection if set true
            channelId: getChannelId(),                   // Channel ID, available in channel settings in ODA UI
            /* START CUSTOMIZATION FOR DEMO*/
            delegate: _delegateObject,
            disablePastActions: 'none',
            enableClearMessage: true,
            enableDraggableButton: true,
            initUserProfile : {profile:{ firstName: 'Frank', lastName: 'Nimphius', email: 'frank.nimphius@oracle.com', timezoneOffset: (new Date()).getTimezoneOffset()*60*1000,properties: {browserLanguage: navigator.language}}},
            height: '1100px',
            width: '800px',
            linkHandler: { target: 'background_frame' },
            webViewConfig: { referrerPolicy: 'no-referrer-when-downgrade', closeButtonType: 'label', closeButtonLabel: 'Close', size: 'full', title: 'Share A Secret' },
            /* END CUSTOMIZATION FOR DEMO*/
            enableAutocomplete: true,                   // Enables autocomplete suggestions on user input
            enableBotAudioResponse: true,               // Enables audio utterance of skill responses
            enableClearMessage: true,                   // Enables display of button to clear conversation
            enableSpeech: true,                         // Enables voice recognition
            speechLocale: WebSDK.SPEECH_LOCALE.EN_US,   // Sets locale used to speak to the skill, the SDK supports EN_US, FR_FR, and ES_ES locales for speech
            showConnectionStatus: true,                 // Displays current connection status on the header
            i18n: {                                     // Provide translations for the strings used in the widget
                en: {                                   // en locale, can be configured for any locale
                    chatTitle: 'Oracle Digital Assistant'    // Set title at chat header
                },
                de: {
                    chatTitle: "Web SDK Anwendungsbeispiele"
                }
            },
            timestampMode: 'relative',                  // Sets the timestamp mode, relative to current time or default (absolute)
            theme: WebSDK.THEME.REDWOOD_DARK,            // Redwood dark theme. The default is THEME.DEFAULT, while older theme is available as THEME.CLASSIC
            messagePadding: '4px 4px'
        };

        // Initialize SDK
        if (isClientAuthEnabled) {
            Bots = new WebSDK(chatWidgetSettings, generateToken);
        } else {
            Bots = new WebSDK(chatWidgetSettings);
        }

        // Connect to skill when the widget is expanded for the first time
        var isFirstConnection = true;
        Bots.on(WebSDK.EVENT.WIDGET_OPENED, function () {
            if (isFirstConnection) {
                Bots.connect();
                isFirstConnection = false;
            }
        });

        // Create global object to refer Bots
        window[name] = Bots;
    }, 0);
}

/**
 * Function to generate JWT tokens. It returns a Promise to provide tokens.
 * The function is passed to SDK which uses it to fetch token whenever it needs
 * to establish connections to chat server
 *
 * @returns {Promise} Promise to provide a signed JWT token
 */
function generateToken() {
    return new Promise(function (resolve) {
        mockApiCall('https://mockurl').then(function (token) {
            resolve(token);
        });
    });
}

/**
 * A function mocking an endpoint call to backend to provide authentication token
 * The recommended behaviour is fetching the token from backend server
 *
 * @returns {Promise} Promise to provide a signed JWT token
 */
function mockApiCall() {
    return new Promise(function (resolve) {
        setTimeout(function () {
            var now = Math.floor(Date.now() / 1000);
            var payload = {
                iat: now,
                exp: now + 3600,
                channelId: '<channelID>',
                userId: '<userID>'
            };
            var SECRET = '<channel-secret>';

            // An unimplemented function generating signed JWT token with given header, payload, and signature
            var token = generateJWTToken({ alg: 'HS256', typ: 'JWT' }, payload, SECRET);
            resolve(token);
        }, Math.floor(Math.random() * 1000) + 1000);
    });
}

/**
 * Unimplemented function to generate signed JWT token. Should be replaced with
 * actual method to generate the token on the server.
 *
 * @param {object} header
 * @param {object} payload
 * @param {string} signature
 */
function generateJWTToken(header, payload, signature) {
    throw new Error('Method not implemented.');
}

function showHideParagraphs(lidx) {
    var dots = document.getElementById("dots" + lidx);
    var moreText = document.getElementById("more" + lidx);
    var btnText = document.getElementById("myBtn" + lidx);
    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "Read more";
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        btnText.innerHTML = "Read less";
        moreText.style.display = "inline";
    }
}
var gidx = 0;

function splitParagraph(txt) {
    var paragraphs = txt.split("##");

    if (paragraphs.length > 1) {
        var html = "<p>" + paragraphs[0] + '<span id="dots' + gidx + '">...</span></p><span id = "more' + gidx + '"class="more" > ';
        for (var idx = 1; idx < paragraphs.length; idx++) {
            html += "<p>" + paragraphs[idx] + "</p>";
        }
        html += '</span><button class="readMore" onclick = "showHideParagraphs(' + gidx + ')" id = "myBtn' + gidx + '" > Readmore</button>';
        gidx++;
        return html;
    }
    else
        return txt;
}

var timer = null;

function resetTimer() {
    if (timer != null) {
        clearTimeout(timer);
    }
    return;
}

function setTimer(lastState, botId, goToState) {

    var _lastState = lastState;
    var _botId = botId;
    var _goToState = goToState;

    //console.log("...."+_lastState+"....."+_botId+"......"+_goToState);
    timer = setTimeout(() => {
        //send message after max. idle time inactivity
        //console.log("...."+_lastState+"....."+_botId+"......"+_goToState);
        Bots.sendMessage({
            "postback": {
                "variables": { "lastState": _lastState },
                "system.botId": _botId,
                //invokes named action transition on system.state or "next" transition
                "action": "",
                "system.state": _goToState
            },
            "text": "Maximum user idle time reached ...",
            "type": "postback"
        });
    },
        //set to 5 seconds of idle time
        5 * 1000
    );
}

function getUri() {
    return "oda-3259ee5123c349feae0c5a062ba9ea97-da6f7264.data.digitalassistant.oci.oraclecloud.com"
}

function getChannelId() {
    return "ff295138-eedd-4bf5-a013-b51cf8b1505b"
}
