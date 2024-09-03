'use strict';

// Set client auth mode - true to enable client auth, false to disable it
var isClientAuthEnabled = false;

/**
 * Initializes the SDK and sets a global field with passed name for it the can
 * be referred later
 *
 * @param {string} name Name by which the chat widget should be referred
 */
function initSdk(name) {
    // Retry initialization later if WebSDK is not available yet
    if (!WebSDK) {
        setTimeout(function() {
            initSdk(name);
        }, 2000);
        return;
    }

    if (!name) {
        name = 'Bots';          // Set default reference name to 'Bots'
    }
    var Bots;

    setTimeout(function() {
        /**
         * SDK configuration settings
         * Other than URI, all fields are optional with two exceptions for auth modes
         * In client auth disabled mode, 'channelId' must be passed, 'userId' is optional
         * In client auth enabled mode, 'clientAuthEnabled: true' must be passed
         */
        var chatWidgetSettings = {
            URI: '<URI>',                               // ODA URI, only the hostname part should be passed, without the https://
            clientAuthEnabled: isClientAuthEnabled,     // Enables client auth enabled mode of connection if set true, no need to pass if set false
            channelId: '<channelID>',                   // Channel ID, available in channel settings in ODA UI
            // userId: '<userID>',                      // User ID, optional field to personalize user experience
            enableAutocomplete: true,                   // Enables autocomplete suggestions on user input
            enableBotAudioResponse: true,               // Enables audio utterance of skill responses
            enableClearMessage: true,                   // Enables display of button to clear conversation
            enableSpeech: true,                         // Enables voice recognition
            speechLocale: WebSDK.SPEECH_LOCALE.EN_US,   // Sets locale used to speak to the skill, the SDK supports EN_US, FR_FR, and ES_ES locales for speech
            showConnectionStatus: true,                 // Displays current connection status on the header
            i18n: {                                     // Provide translations for the strings used in the widget
                en: {                                   // en locale, can be configured for any locale
                    chatTitle: '<Chat Header Title>'    // Set title at chat header
                }
            },
            timestampMode: 'relative',                  // Sets the timestamp mode, relative to current time or default (absolute)
            theme: WebSDK.THEME.REDWOOD_DARK            // Redwood dark theme. The default is THEME.DEFAULT, while older theme is available as THEME.CLASSIC
        };

        // Initialize SDK
        if (isClientAuthEnabled) {
            Bots = new WebSDK(chatWidgetSettings, generateToken);
        } else {
            Bots = new WebSDK(chatWidgetSettings);
        }

        // Connect to skill when the widget is expanded for the first time
        var isFirstConnection = true;
        Bots.on(WebSDK.EVENT.WIDGET_OPENED, function() {
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
    return new Promise(function(resolve) {
        mockApiCall('https://mockurl').then(function(token) {
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
    return new Promise(function(resolve) {
        setTimeout(function() {
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
