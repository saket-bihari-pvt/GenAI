<!-- omit in toc -->
# Web SDK

Use Oracle Digital Assistant's Client SDK for JavaScript to add live messaging to your website or web app.

- [Installation](#installation)
  - [HTML script tag](#html-script-tag)
  - [Importing SDK library in JavaScript](#importing-sdk-library-in-javascript)
  - [Import the Library Using the Asynchronous Module Definition API](#import-the-library-using-the-asynchronous-module-definition-api)
- [Browser Support](#browser-support)
- [SDK Security](#sdk-security)
  - [Channel with Client Auth Disabled](#channel-with-client-auth-disabled)
  - [Channel with Client Auth Enabled](#channel-with-client-auth-enabled)
  - [JWT Token](#jwt-token)
- [Settings](#settings)
  - [Network Configuration](#network-configuration)
  - [Feature Flags](#feature-flags)
  - [Functionality Configuration](#functionality-configuration)
  - [Layout Modification](#layout-modification)
  - [Custom Colors](#custom-colors)
  - [Custom Icons](#custom-icons)
  - [Custom Text](#custom-text)
  - [Customizing CSS Classes](#customizing-css-classes)
- [Enums](#enums)
  - [WebSDK.EVENT](#websdkevent)
  - [WebSDK.SPEECH_LOCALE](#websdkspeech_locale)
  - [WebSDK.THEME](#websdktheme)
- [Methods](#methods)
  - [connect()](#connect)
  - [connect(config)](#connectconfig)
  - [disconnect()](#disconnect)
  - [isConnected()](#isconnected)
  - [openChat()](#openchat)
  - [closeChat()](#closechat)
  - [isChatOpened()](#ischatopened)
  - [destroy()](#destroy)
  - [sendAttachment(file)](#sendattachmentfile)
  - [sendMessage(message, flags)](#sendmessagemessage-flags)
  - [updateUser(userDetails)](#updateuseruserdetails)
  - [getSuggestions(query)](#getsuggestionsquery)
  - [startVoiceRecording(onSpeechRecognition, onSpeechNetworkChange, options)](#startvoicerecordingonspeechrecognition-onspeechnetworkchange-options)
  - [stopVoiceRecording()](#stopvoicerecording)
  - [setSpeechLocale(locale)](#setspeechlocalelocale)
  - [setPrimaryLanguage(languageTag)](#setprimarylanguagelanguagetag)
  - [setSkillVoices(voices)](#setskillvoicesvoices)
  - [setDelegate(delegate)](#setdelegatedelegate)
  - [getConversationHistory()](#getconversationhistory)
  - [clearConversationHistory(userId, shouldClearWidget)](#clearconversationhistoryuserid-shouldclearwidget)
  - [clearAllConversationsHistory(shouldClearWidget)](#clearallconversationshistoryshouldclearwidget)
  - [getUnreadMessagesCount()](#getunreadmessagescount)
  - [setAllMessagesAsRead()](#setallmessagesasread)
  - [setUserInputMessage(text)](#setuserinputmessagetext)
  - [setUserInputPlaceholder(text)](#setuserinputplaceholdertext)
  - [showTypingIndicator()](#showtypingindicator)
  - [setWebViewConfig(webViewConfig)](#setwebviewconfigwebviewconfig)
  - [setChatBubbleIconHeight(height)](#setchatbubbleiconheightheight)
  - [setChatBubbleIconWidth(width)](#setchatbubbleiconwidthwidth)
  - [setChatBubbleIconSize(width, height)](#setchatbubbleiconsizewidth-height)
  - [setFont(font)](#setfontfont)
  - [setFontFamily(fontFamily)](#setfontfamilyfontfamily)
  - [setFontSize(fontSize)](#setfontsizefontsize)
  - [setHeight(height)](#setheightheight)
  - [setWidth(width)](#setwidthwidth)
  - [setSize(width, height)](#setsizewidth-height)
  - [setMessagePadding(padding)](#setmessagepaddingpadding)
  - [setTextColor(color)](#settextcolorcolor)
  - [setTextColorLight(color)](#settextcolorlightcolor)
- [Events](#events)
  - [ready](#ready)
  - [destroy](#destroy-1)
  - [message:received](#messagereceived)
  - [message:sent](#messagesent)
  - [message](#message)
  - [networkstatuschange](#networkstatuschange)
  - [typing](#typing)
  - [unreadCount](#unreadcount)
  - [widget:opened](#widgetopened)
  - [widget:closed](#widgetclosed)
  - [click:audiotoggle](#clickaudiotoggle)
  - [click:erase](#clickerase)
  - [click:voicetoggle](#clickvoicetoggle)
  - [chatlanguagechange](#chatlanguagechange)
- [Features](#features)
  - [Autocomplete](#autocomplete)
  - [Delegation](#delegation)
    - [beforeDisplay](#beforedisplay)
    - [beforeSend](#beforesend)
    - [beforePostbackSend](#beforepostbacksend)
  - [Embedded mode](#embedded-mode)
  - [Headless SDK](#headless-sdk)
  - [In-Widget WebView](#in-widget-webview)
  - [Long Polling](#long-polling)
  - [Multi-Lingual Chat](#multi-lingual-chat)
  - [Response narration](#response-narration)
  - [Voice Recognition](#voice-recognition)
  - [Absolute and Relative Timestamps](#absolute-and-relative-timestamps)
- [Customizations](#customizations)
  - [Add avatar icons with messages](#add-avatar-icons-with-messages)
  - [Change header buttons icons](#change-header-buttons-icons)
  - [Draggable launch button](#draggable-launch-button)
  - [Focus first action of skill message](#focus-first-action-of-skill-message)
  - [Format message timestamps](#format-message-timestamps)
  - [Opening Links](#opening-links)
  - [Relative Timestamps](#relative-timestamps)
  - [Restrict attachment types](#restrict-attachment-types)
    - [Custom share menu items](#custom-share-menu-items)
- [Message Model](#message-model)
  - [Base Types](#base-types)
    - [Action](#action)
      - [PostbackAction](#postbackaction)
      - [CallAction](#callaction)
      - [UrlAction](#urlaction)
      - [ShareAction](#shareaction)
      - [LocationAction](#locationaction)
    - [Attachment](#attachment)
    - [Card](#card)
    - [Location](#location)
  - [Conversation Messages](#conversation-messages)
  - [Message](#message-1)
  - [User Message](#user-message)
    - [User Text Message](#user-text-message)
    - [User Attachment Message](#user-attachment-message)
    - [User Location Message](#user-location-message)
    - [User Postback Message](#user-postback-message)
  - [Skill Message](#skill-message)
    - [Skill Text Message](#skill-text-message)
    - [Skill Attachment Message](#skill-attachment-message)
    - [Skill Location Message](#skill-location-message)
    - [Skill Postback Message](#skill-postback-message)
    - [Skill Card Message](#skill-card-message)
    - [Skill Raw Message](#skill-raw-message)
- [Limitations](#limitations)

## Installation

### HTML script tag

1. First, save `web-sdk.js` in your project directory. Keep note of its location.
2. Add the following code towards the end of the `head` section on your HTML page.  Replace `<Server URI>` with location of `web-sdk.js`, and `<WebSDK namespace>` with a name for the library, which is typically `Bots`. The library will be referred by that name and used to make the API calls.
```html
<script>
    var chatSettings = {
        URI: '<Server URI>',
        channelId: '<Channel ID>',
        userId: '<User ID>'
    };

    function initSDK(name) {
        // If WebSDK is not available, reattempt later
        if (!WebSDK) {
            setTimeout(function() {
                initSDK(name);
            }, 2000);
            return;
        }

        // Default name is Bots
        if (!name) {
            name = 'Bots';
        }

        setTimeout(function() {
            var Bots = new WebSDK(chatSettings);    // Initiate library with configuration
            Bots.connect()                          // Connect to server
                .then(function() {
                   console.log('Connection Successful');
               })
               .catch(function(reason) {
                   console.log('Connection failed');
                   console.log(reason);
               });

           window[name] = Bots;
        }, 0);
    }
</script>
<script src="<WebSDK URL>" onload="initSDK('<WebSDK namespace>')">
```

You need to make a few minor modifications if you're connecting to a channel with client authentication enabled. Along with setting the `clientAuthEnabled` property to `true`, you must also include a function that generates and passes a JWT token. The function must return a `Promise` that resolves to a signed JWT token string. The SDK will use this function to generate a new token whenever it needs to establish a new connection because the existing token has expired. The script would look something like this:

```html
<script>
    var chatSettings = {
        URI: '<Server URI>',
        clientAuthEnabled: true
    };

    function initSDK(name) {
        // If WebSDK is not available, reattempt later
        if (!WebSDK) {
            setTimeout(function() {
                initSDK(name);
            }, 2000);
            return;
        }

        // Default name is Bots
        if (!name) {
            name = 'Bots';
        }

        setTimeout(function() {
            var Bots = new WebSDK(chatSettings);    // Initiate library with configuration
            Bots.connect()                          // Connect to server
                .then(function() {
                   console.log('Connection Successful');
               })
               .catch(function(reason) {
                   console.log('Connection failed');
                   console.log(reason);
               });

           window[name] = Bots;
        }, 0);
    }

    function generateToken() {
        return new Promise(function(resolve) {
            fetch('https://yourbackend.com/endpointToGenerateJWTToken').then(function(token) {
                resolve(token);
            })
        });
    }
</script>
<script src="<WebSDK URL>" onload="initSDK('<WebSDK namespace>')">
```

*Et voila!* You have an app integrated with Oracle Web SDK.

### Importing SDK library in JavaScript

To import the library dynamically in JavaScript, use the following utility function,  which is based on the [MDN example](https://developer.mozilla.org/en-US/docs/Web/API/HTMLScriptElement#Dynamically_importing_scripts) for importing scripts dynamically:

```js
function fetchSDK(src, onloadFunction, name) {
    var script = document.createElement('script');
    script.type = 'application/javascript';
    script.async = true;    // load the script asynchronously
    script.defer = true;    // fallback support for browsers that does not support async
    script.onload = function() {
        onloadFunction(name);
    };
    document.head.appendChild(script);
    script.src = src;
}

fetchSDK('<path of the web-sdk>', initSDK, '<WebSDK namespace>');
```

### Import the Library Using the Asynchronous Module Definition API

You can import the library using implementations of the Asynchronous Module Definition (AMD) API such as RequireJS with Oracle JET, and SystemJS.

```js
requirejs(['<path of the web-sdk>'], function(WebSDK) {
    var settings = {
        URI: '<Server URI>',
        channelId: '<Channel ID>',
        userId: '<User ID>'
    };
    Bots = new WebSDK(settings);

    Bots.connect();
});

```

## Browser Support
The SDK is supported on these browsers on Mac, Windows, and Linux:
* Firefox
* Chrome
* Safari
* Edge

For mobile platforms the following browsers are supported:
* Android browser
* iOS Safari

## SDK Security

The Web SDK can connect to the Oracle Digital Assistant web channel in two modes: client auth disabled and client auth enabled.

### Channel with Client Auth Disabled

When client authentication has been disabled, only connections made from unblocked lists (allowed domains) are allowed at the server. This use case is recommended when the client application can’t generate a signed JWT Token (because of a static website or no authentication mechanism for the web/mobile app) but requires ODA integration. It can also be used when the chat widget is already secured and visible to only authenticated users in the client platforms (Web Application with protected page).

When connecting to such channels, `channelId` must be passed as a setting parameter during SDK initialization. The `userId` is also required to establish the connection. If you don't provide a value during initialization, then the SDK generates a random `userId`.

```js
{
    URI: 'oda-instance.com',
    channelId: '626f5db1-f99a-4984-86ee-df2d734537e6',
    userId: 'Jessica'
}
```

### Channel with Client Auth Enabled

In addition to unblocked lists, client authentication is enforced by signed JWT tokens.

The token generation and signing must be done by the client in the backend server ( preferably after user/client authentication) which is capable of maintaining the `keyId` and `keySecret` safe.

When the SDK needs to establish a connection with the ODA server, it first requests a JWT token from the client and then sends it along with the connection request. The ODA server validates the token signature and obtains the claim set from the JWT payload to verify the token to establish the connection.

To enable this mode, these two fields are required during SDK initialization: `clientAuthEnabled: true` must be passed in the SDK settings parameter, and a **token generator function** must be passed as the second parameter. The function must return a `Promise`, which is resolved to return a signed JWT token string.

```js
function generateToken() {
    return new Promise(function(resolve) {
        fetch('https://yourbackend.com/endpointToGenerateJWTToken').then(function(token) {
            resolve(token);
        });
    });
}

Bots.init({
    URI: 'oda-instance.com',
    clientAuthEnabled: true
}, generateToken);
```

### JWT Token

The JWT token generation and signing are the responsibility of the client application. Some of the token payload fields are mandatory and are validated by the ODA server.

Clients must use the HS256 signing algorithm to sign the tokens. The tokens must be signed by the secret key of the client auth enabled channel to which the connection is made. The body of the token must have the following claims:

* `iat` - issued at time - must be a number representing seconds since UNIX epoch
* `exp` - expiry time - must be a number representing seconds since UNIX epoch
* `channelId` - channel ID - must be a string
* `userId` - user ID - must be a string

Here's a sample signed JWT token:

Encoded token:

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzY3NDcyMDUsImV4cCI6MTU3Njc1MTExNywiY2hhbm5lbElkIjoiNDkyMDU5NWMtZWM3OS00NjE3LWFmOWYtNTk1MGQ2MDNmOGJiIiwidXNlcklkIjoiSm9obiIsImp0aSI6ImQzMjFjZDA2LTNhYTYtNGZlZS05NTBlLTYzZGNiNGVjODJhZCJ9.lwomlrI6XYR4nPQk0cIvyU_YMf4gYvfVpUiBjYihbUQ
```

Decoded token:

Header:

```json
{
    "typ": "JWT",
    "alg": "HS256"
}
```

Payload:

```json
{
    "iat": 1576747205,
    "exp": 1576748406,
    "channelId": "4920595c-ec79-4617-af9f-5950d603f8bb",
    "userId": "John"
}
```

> If any claim in the token is missing or has incorrect format for its value, an error message is thrown by the SDK describing the cause, and the connection is not attempted. The error message can be used to fix the issue with the JWT token.

Any additional claims passed in the payload do not affect the client authentication mechanism.

## Settings

Use these properties to configure the chat widget:

### Network Configuration
| Property name | Optional | Default Value | Description |
| ------ | ------ | ------ | ------ |
| `URI` | No || Host name in ODA instance URL. Only the host section between the URL scheme, `https://`, and first path, `/`, needs to be passed here. |
| `channelId` | No || The Web Channel ID |
| `userId` | Yes | Random generated value | A unique identifier for user. This ID gets initialized by SDK if one has not been provided. |
| `clientAuthEnabled` | Yes | `false` | Determines whether the SDK is connecting to a client authentication-enabled channel. This must be set to `true` to connect to such a channel and use a JWT token for authentication. |

### Feature Flags
| Property name | Default Value | Description |
| ------ | ------ | ------ |
| **`delegate`** || An object that enables you to set a delegate to receive callbacks before certain events in the conversation. See [Delegation](#delegation) for more details. |
| **`embedded`** | `false` | Embeds the chat widget inside another element referened by `targetElement` setting. See [Embedded mode](#embedded-mode) for more details. |
| `targetElement` || The ID of the HTML element in DOM, such as a `div`, in which the chat widget is embedded. to embed the chat widget. Must be passed when `embedded` is set `true`. The element must have some dimensions (height and width), as the widget takes the dimensions of this container. |
| **`enableAttachment`** | `true` | Enables user to share files and location |
| `enableAttachmentSecurity` | `false` | *Only applicable for client auth enabled connections to ODA platform version 20.12 and above*. When set `true`, extra headers are passed to the attachment upload requests to ensure that they can't be downloaded without passing a valid signed JWT token in the URL as value of `token` query parameter in the attachment fetch request URL. The setting must not be enabled if connecting to an ODA instance Version 20.08 or older for compatibility. |
| `shareMenuItems` | `['audio', 'file', 'location', 'visual']` | The categories shown in the share popup menu. Accepts an array with string values mapped to menu items - `'visual'` for image and videos, `'audio'` for audio, `'file'` for files, and `'location'` for location. Only the categories for passed values are shown in the menu. If no/incorrect values are passed, all menu categories are shown. Also allows passing custom share items. See [Restrict attachment types](#restrict-attachment-types) for more details on the flag and passing custom menu items. |
| **`enableAutocomplete`** | `false` | Provides autocomplete suggestions as a user types a message in the input field. See [Autocomplete](#autocomplete) for more details. |
| `enableAutocompleteClientCache` | `false` | Enables client side caching to minimize server calls when the user uses the autocomplete feature |
| **`enableBotAudioResponse`** | `false` | Enables the utterance of a skill's responses as they are received using the Web speech synthesis API. See [Response narration](#response-narration) for more details. |
| `initBotAudioMuted` | `true` | Initializes the skill message utterance in muted mode. Only applicable when `enableBotAudioResponse` is `true`. |
| `skillVoices` | System language | An array containing preferred voices used for narrating responses. Each item in the array should be an object with two fields: `lang`, and `name`. `name` is optional. The first item that matches a voice that’s available in the system will be used for the narration. |
| **`enableHeadless`** | `false` | Initializes SDK instances without its chat widget while exposing its methods. Enables you to develop your own UI for the chat. See [Headless SDK](#headless-sdk) for more details. |
| **`enableLongPolling`** | `false` | Enables use of HTTP-based communication with the skill as a fallback if the WebSocket connection fails. See [Long Polling](#long-polling) for more details. |
| **`enableSpeech`** | `false` | Enables voice recognition service to allow the user to converse with the skill using voice messages by converting their voice input to text message. See [Voice Recognition](#voice-recognition) for more details. |
| `enableSpeechAutoSend` | `true` | Automatically sends voice recognized text to the skill |
| `speechLocale` | `'en-us'` | The locale of the voice recognition the user is expected to speak in. The supported locales are `'en-us`, `'es-es'`, `'fr-fr'`, and `'pt-br'`. |
| **`enableTimestamp`** | `true` | Displays timestamp below messages as they are seen by the user. See [Absolute and Relative Timestamps](#absolute-and-relative-timestamps) for more details. |
| `timestampFormat` | `{ weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }` | Allows the formatting of the delivery timestamp shown with messages. Accepts values in [DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#Syntax) options object or a pattern string. See  [Format message timestamps](#format-message-timestamps) for more details. |
| `timestampMode` | `'default'` | Selects the timestamp format as either absolute timestamps that appear on each message when set `'default'`, or as a relative timestamp that appears only on the latest message, when set `'relative'`. See [Relative Timestamps](#relative-timestamps) for more details. |
| **`multiLangChat`** | | Enables the chat widget to both detect a user's language and allow the user to select a preferred language from a dropdown menu in the header for conversation. See [Multi-Lingual Chat](#multi-lingual-chat) for more details. |
| **`webViewConfig`** | `{ referrerPolicy: 'no-referrer-when-downgrade', closeButtonType: 'icon', size: 'tall' }` | Enables customizations to the in-widget webview, including its clear button, its header, and the partial or full-screen sizing of the webview itself. See [In-Widget WebView](#in-widget-webview) for more details. |

### Functionality Configuration
| Property name | Default Value | Description |
| ------ | ------ | ------ |
| `customHeaderElementId` || The ID of the element to add to the chat widget header. Used for adding additional elements to the chat widget header. |
| `disablePastActions` | `'all'` | Disables action buttons in a skill message once user has interacted with it. When set to `all`, all action buttons of the message are disabled upon interaction. Setting `postback` only disables postback and location messages, and setting `none` keeps all buttons enabled even after interaction. |
| `displayActionsAsPills` | `false` | Displays action buttons as pills |
| `embeddedVideo` | `false` | Embeds YouTube video links to be playable within chat widget if passed in the messages if set `true` |
| `embedBottomScrollId` || The ID of the element to be added as a scrollable content at bottom of chat. The element must be a part of the DOM. |
| `embedBottomStickyId` || The ID of the element to be added as a pinned content at bottom of chat. The element must be a part of the DOM. |
| `embedTopScrollId` || The ID of the element to be added as a scrollable content at top of chat. The element must be a part of the DOM. |
| `embedTopStickyId` || The ID of the element to be added as a pinned content at top of chat. The element must be a part of the DOM. |
| `enableClearMessage` | `false` | Displays a 'clear messages' button in the chat widget header |
| `enableDraggableButton` | `false` | Enables users to drag the launch button out of the way when it's blocking content on the page. See [Draggable launch button](#draggable-launch-button) for more details. |
| `enableLocalConversationHistory` | `false` | Loads previous conversations for a passed userId on the current browser when the chat widget is initialized |
| `focusOnNewMessage` | `'input'` | Sets the focus on either the user input field, or on the first action button in a message when a new message is received. When set to `'action'`, the focus is the first action button (if the message has action buttons) when a message is received. If the message has no buttons, then the focus is the user input field. When set to `'input'`, the user input field remains as the focus when new messages are received. See [Focus first action of skill message](#focus-first-action-of-skill-message) for more details. |
| `i18n` | `{'en': {...}}` | The object that contains locale fields; each locale maintains i18n key-value pairs for certain strings that are used in the widget. See [Custom Text](#custom-text) for the strings that you can customize. |
| `initUserHiddenMessage` || A user message to send once the chat widget is expanded and connected to the skill, without displaying the message in the chat widget. Used to initiate the conversation automatically. The message can be a text string, like `'Hi'`, or a message object, like `{ type: 'text', text: 'Hi'}`, or `{ messagePayload: { type: 'text', text: 'Hi'}}`. |
| `initUserProfile` || Initializes the user profile before the conversation starts. The profile payload must be of format `{ profile: {...} }`. The profile is updated before sending the value in `initUserHiddenMessage`. |
| `initMessageOptions` | `{ sendAt: 'expand' }` | Customizes the `initUserHiddenMessage` and `initUserProfile` behavior. It accepts an object with a `sendAt` property that can be set to either `'expand'` or `'init'`. If set `'expand'`, the init messages are sent once the chat widget is expanded. If set `'init'` on the other hand, the init messages are sent immediately on connection, whether the widget is expanded or not. |
| `isDebugMode` | `false` | Allows the SDK to log statements in console for debugging purposes |
| `linkHandler` | `{ onclick: <function>, target: 'string' }` | An object that overrides the configuration for handling the clicks on the links that are embedded in the skill's responses. This object handles links in two ways, setting link's target in field `target` which accepts a string, and/or adding a click event listener in field `onclick`. When you want all links to open in WebView, pass `linkHandler: { target: 'oda-chat-webview'}`. See [Opening Links](#opening-links) for more details. |
| `locale` | `'en'` | The default locale which is used for the informational text in the SDK. The locale passed has higher preference over users' browser locales. If there isn't an exact match, then the SDK attempts to match the closest language. For example, if the locale is `'da-dk'`, but i18n translations are provided only for `'da'`, then the `'da'` translation is used. In absence of translations for passed locale, translations are searched and applied for browser locales. In absence of translations for any of them, the default locale, `'en'` is used for translations. |
| `messageCacheSizeLimit` | `2000` | Maximum number of messages to be saved in localStorage at a time |
| `openChatOnLoad` | `false` | Expands chat widget when the SDK instance is initialized |
| `openLinksInNewWindow` | `false` | If set to `true`, the target is opened in a new window when a link in a message is clicked. The browser's preference is not followed. See [Opening Links](#opening-links) for more details. |
| `readMark` | `'✓'` | Sets the symbol that denotes that a skill's message has been seen. This symbol is displayed along with the timestamp, and not disabled if `enableTimestamp` is set `false`. |
| `showConnectionStatus` | `false` | Displays current connection status in chat header below title |
| `showPrevConvStatus` | `true` | Displays a status message at the end of messages from previous conversations for given userId |
| `showTypingIndicator` | `true` | Displays an indicator in conversation pane while waiting for the skill's response |
| `storageType` | `'localStorage'` | A web storage mechanism that is used to store the conversation history of users whose `userId` is passed by the host app. The supported values are `'localStorage'` and `'sessionStorage'`. Anonymous users' conversations are always stored in `sessionStorage`, and deleted automatically when the browser session ends. |
| `theme` | `'default'` | Chat widget theme. The supported values are `'default'`, a dark blue theme, `'redwood-dark`, a dark redwood theme, and `'classic'`, a light blue theme. |
| `typingIndicatorTimeout` | `20` | Allows setting the time in the number of seconds after which the typing indicator is automatically removed if the chat widget has not yet received the response. |

### Layout Modification
| Property name | Default Value | Description |
| ------ | ------ | ------ |
| `badgePosition` | `{top: '0', right: '0'}` | The position of the notification badge icon with respect to the skill button |
| `colors` | `{branding: '#1B8FD2', text: '#212121', textLight: '#737373'}` | The colors used in the chat widget. See [Custom Colors](#custom-colors) for more details. |
| `conversationBeginPosition` | `'top'` | The starting position of the conversation in the widget. If set to `'top'`, the first messages appear on the top of widget. If `'bottom'`, they appear on the bottom. |
| `font` | `'16px "Helvetica Neue", Helvetica, Arial, sans-serif'` | (*Obsolete*) Font for chat widget. Use `fontFamily` instead. |
| `fontFamily` | `'"Oracle Sans", "Helvetica Neue", Helvetica, Arial, sans-serif'` | Font family used for all text in the chat widget. |
| `height` | `'620px'` | The height of the chat widget. Must be set to one of [length](https://developer.mozilla.org/en-US/docs/Web/CSS/length) values |
| `messagePadding` | `'15px'` | Padding around messages in chat widget |
| `position` | `{bottom: '20px', right: '20px'}` | A field to specify where to place the chat widget in the browser window. Must be passed as a JSON object |
| `width` | `'375px'` | The width of the chat widget. Must be set to one of [length](https://developer.mozilla.org/en-US/docs/Web/CSS/length) values |

### Custom Colors

The following colors can be modified to provide a custom look for the widget. The color provided must be a hexadecimal color. If a color is not provided, the default is used.

| key | Description |
| ------ | ------ |
| `branding` | The primary color for branding the widget. The color is used as the header background, and as hover color on footer buttons. |
| `text` | The text color of the messages in the chat widget. Gets overridden if component specific setting is applied. |
| `textLight` | The text color of secondary text in messages, e.g., card descriptions in chat widget |
| `headerBackground` | The background color of the chat widget's header |
| `headerButtonFill` | The SVG fill color of buttons in the chat header |
| `headerText` | The color of title in the chat header |
| `conversationBackground` | The background of the chat widget's conversation pane. It accepts all values supported by `background` [CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/background), so it can be used to set image backgrounds, gradients, etc. as well. |
| `botMessageBackground` | The skill message background color |
| `botText` | The skill text color. Overrides the `text` color if passed. |
| `userMessageBackground` | The user message background color |
| `userText` | The user text color. Overrides the `text` color if passed. |
| `actionsBackground` | The action button background color |
| `actionsBackgroundHover` | The action button background color on hover |
| `actionsBackgroundFocus` | The action button background color on focus |
| `actionsBorder` | The action button border color |
| `actionsText` | The action button text color |
| `actionsTextHover` | The action button text color on hover |
| `actionsTextFocus` | The action button text color on focus |
| `globalActionsBackground` | The global action button background color |
| `globalActionsBackgroundHover` | The global action button background color on hover |
| `globalActionsBackgroundFocus` | The global action button background color on focus |
| `globalActionsBorder` | The global action button border color |
| `globalActionsText` | The global action button text color |
| `globalActionsTextHover` | The global action button text color on hover |
| `globalActionsTextFocus` | The global action button text color on focus |
| `cardBackground` | The card message's background color |
| `cardNavButton` | The card navigation button background color |
| `cardNavButtonHover` | The card navigation button background color on hover |
| `cardNavButtonFocus` | The card navigation button background color on focus |
| `links` | The color of the links that are embedded in messages |
| `timestamp` | The color of the timestamp header and the relative timestamp in messages |
| `typingIndicator` | The background fill color of the typing indicator |
| `footerBackground` | The background color of the chat widget's footer |
| `footerButtonFill` | The SVG fill color of the buttons in chat footer |
| `inputBackground` | The background color of the message input field |
| `inputText` | The text color in the message input field. Overrides `text` if passed. |
| `recognitionViewBackground` | The background color of the recognition text view, which is displayed in voice mode. If absent, the header background color is used. |
| `recognitionViewText` | The text color in recognition text view displayed in voice mode. If absent, text color is used. |
| `recognitionViewButtonFill` | The SVG fill color of the mode toggle color in voice mode |
| `visualizerContainerBackground` | The background color of the visualizer container displayed in voice mode. If absent, user message background color is used. |
| `visualizer` | The color used in bars of the visualizer graph. If absent, branding color is used. |
| `notificationBadgeBackground` | The background color of the message notification badge |
| `notificationBadgeText` | The text color of message count in notification badge |

Here's an example of providing a custom color.
```js
colors: {
    branding: '#e00',
    text: '#545454'
}
```
The branding and text color will be modified in above example. Default color is used for secondary text color.

### Custom Icons

The icons used in the widget can be customized in two ways - the URL of the image asset, or an SVG string. For the icons that support SVG strings, you can pass the raw SVG data which the widget renders as an inline SVG. SVG strings allow for the faster loading of an image, the ability to animate it, or for changing its color. The theme color is applied to SVG strings for attachment, send, and mic buttons, but not other image assets.

| Property name | SVG String Compatible | Description |
| ------ | ------ | ------ |
| `botButtonIcon` | No | The chat bot button that's displayed as the minimized chat button |
| `logoIcon` | No | The chat logo icon that's displayed at the header of the chat widget |
| `agentAvatar` | No | The Avatar icon that's displayed alongside the response messages coming from a live agent. If not provided, and `botIcon` is provided, then the `botIcon` is displayed. If neither `agentAvatar` or `botIcon` are provided, then no icon is displayed. |
| `botIcon` | No | the icon alongside skill response messages. If not provided, no icon is displayed. |
| `personIcon` | No | The icon that displays alongside user messages. If not provided, no icon is displayed |
| `chatBubbleIcon` | The loading chat bubble icon |
| `clearMessageIcon` | The clear message button icon at widget header |
| `audioResponseOffIcon` | The icon of toggle button when audio responses are turned off |
| `audioResponseOnIcon` | The icon of toggle button when audio responses are turned on |
| `closeIcon` | The icon for the button to minimize chat widget at widget header |
| `attachmentIcon` | The attachment upload button icon |
| `sendIcon` | The send message button icon |
| `keyboardIcon` | The keyboard icon, displayed in button to switch from voice to keyboard mode |
| `micIcon` | The mic icon, displayed in button to switch from keyboard to voice mode |
| `audioIcon` | No | The audio attachment icon, displayed when attachment source URL is not reachable |
| `fileIcon` | No | The file attachment icon |
| `imageIcon` | No | The image attachment icon, displayed when attachment source URL is not reachable |
| `videoIcon` | No | The video attachment icon, displayed when attachment source URL is not reachable |
| `errorIcon` | No | The error icon. Displayed with error messages or information  |

| Property name | Optional | Default Value | Description |
| ------ | ------ | ------ | ------ |
| `chatBubbleIconHeight` | `'42px'` | Height of loading chat bubble icon |
| `chatBubbleIconWidth` | `'56px'` | Width of loading chat bubble icon |

Here's an example of providing custom icons:
```js
var chatSettings = {
    ...,
    clearMessageIcon: 'https://cdn4.iconfinder.com/data/icons/kids-2/128/kids_kid_boy-32.png',
    micIcon: '<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0z" fill="none" opacity=".1"/><path d="M12 1c-4.97 0-9 4.03-9 9v7c0 1.66 1.34 3 3 3h3v-8H5v-2c0-3.87 3.13-7 7-7s7 3.13 7 7v2h-4v8h4v1h-7v2h6c1.66 0 3-1.34 3-3V10c0-4.97-4.03-9-9-9z"/></svg>'
};
```

### Custom Text
The following strings can be customized to provide localized text. The strings must be provided under a valid [language string](https://www.science.co.il/language/Locale-codes.php) e.g. 'en-us', 'es', 'fr', 'zh-cn'.

| key | Default Value | Description |
| ------ | ------ | ------ |
| `attachmentAudioFallback` | `'Your browser does not support embedded audio. However you can {0}download it{/0}.'` | The fallback message that is displayed in place of an audio attachment if the audio can not be rendered by the client. The text between `{0}` and `{/0}` is set to a link to download the file. |
| `attachmentVideoFallback` | `'Your browser does not support embedded video. However you can {0}download it{/0}.'` | The fallback message that's displayed in place of an video attachment if the video can not be rendered by the client. The text between `{0}` and `{/0}` is set to a link to download the file. |
| `audioResponseOff` | `'Turn audio response on'` | The tooltip that appears when hovering over the audio utterance on button in header. |
| `audioResponseOn` | `'Turn audio response off'` | The tooltip that appears when hovering over the audio utterance off button in header. |
| `card` | `'Card'` | CRC Card identifier. |
| `cardImagePlaceholder` | `'Card image'` | The text placeholder that's displayed while the card image is fetched and loaded. |
| `cardNavNext` | `'Next card'` | The card navigation button label that displays the next card in horizontal layout. |
| `cardNavPrevious` | `'Previous card'` | The card navigation button label that displays the previous card in horizontal layout. |
| `chatTitle` | `'Chat'` | Title of the chat widget that is displayed on the header.  |
| `chatSubtitle` || The subtitle of the chat widget that's displayed on the header below the title. If `showConnectionStatus` is set to `true`, and the subtitle is set as well, then the subtitle displays in place of the connection status. |
| `clear` | `'Clear conversation'` | The tooltip that appears when hovering over clear messages button in header. |
| `close` | `'Close widget'` | The tooltip that appears when hovering over close widget button in header. |
| `closing` | `'Closing'` | The status text when the connection between the chat widget and the server is closing. |
| `connected` | `'Connected'` | The status text when the connection between the chat widget and the server is established. |
| `connecting` | `'Connecting'` | The status text when the connection between the chat widget and the server is connecting. |
| `disconnected` | `'Disconnected'` | The status text when the connection between the chat widget and the server is closed. |
| `errorSpeechInvalidUrl` | `'Speech server URL not set. Can\'t start recording.'` | The error message that is displayed when the voice server URL is invalid or not set. |
| `errorSpeechMultipleConnection` | `'A voice recognition connection is live. Can\'t start another connection.'` | The error message that's displayed when the user attempts a new voice message while another recognition is ongoing. This usually happens when multiple voice connections are attempted in short interval by repeatedly toggling between keyboard and voice mode. |
| `errorSpeechTooMuchTimeout` | `'Too much voice input to recognize. Can\'t generate recognized text.'` | The error message that's displayed when the user provides a voice message that can't be recognized because it's too long. |
| `errorSpeechUnavailable` | `'Microphone is not accessible in this browser. Can't start recording.'` | The error message that's displayed when the browser does not provide any API to access the microphone. |
| `errorSpeechUnsupportedLocale` | `'The set speech locale is not supported. Can\'t start recording.'` | The error message that's displayed when an unsupported speech locale is configured for voice recognition and a recording is attempted. |
| `inputPlaceholder` | `'Type a message'` | The placeholder text that appears in the user input field in keyboard mode. |
| `noSpeechTimeout` | `'Could not detect the voice, no message sent.'` | The status text that's displayed when the server is unable to recognize the voice. |
| `language_detect` | `'Detect Language'` | The label for auto-detect option in language selection dropdown. |
| `language_<languageTag>` | *`Language Label`* | The label for the language represented by the `languageTag`, e.g. 'English' for 'en' in the language selection dropdown available when  [Multi-Lingual Chat](#multi-lingual-chat) is configured. |
| `openMap` | `'Open Map'` | Label of the action button to open a location map. |
| `previousChats` | `'Previous conversations'` | The status text that's displayed at the end of older messages. |
| `recognitionTextPlaceholder` | `'Speak your message'` | Placeholder text that appears in recognition text field in voice mode. |
| `requestLocation` | `'Requesting location'` | Text that is displayed while user location is requested on browser. |
| `requestLocationDeniedPermission` | `'Location permission denied. Please allow access to share your location, or else type in your location.'` | The error message that's displayed when permission to access location is denied. |
| `requestLocationDeniedTimeout` | `'Taking too long to get your current location. Please try again, or else type in your location.'` | The error message that's displayed when location request is not resolved due to a timeout. |
| `requestLocationDeniedUnavailable` | `'Your current location is unavailable. Please try again, or else type in your location.'` | The error message that is displayed when location request is denied due to unavailability of current location in client's device. |
| `retryMessage` | `'Try again'` | Text that is displayed when user message is not sent to server. |
| `send` | `'Send message'` | Tooltip that appears when hovering over send button in footer. |
| `shareAudio` | `'Share Audio'` | The menu item text for sharing an audio file in the share popup. |
| `shareFile` | `'Share File'` | The menu item text for sharing a generic file in the share popup. |
| `shareLocation` | `'Share Location'` | The menu item text for sharing a location in the share popup. |
| `shareVisual` | `'Share Image/Video'` | The menu item text for sharing an image or video file in the share popup. |
| `shareFailureMessage` | `'Sorry, sharing is not available on this device.'` | The error message that's shown when a user clicks on a share action button and the share API is not supported by the device. |
| `skillMessage` | `'Skill says'` | The skill message indicator for screen readers. It is spoken by the screen readers before the skill responses. |
| `speak` | `'Speak a message'` | The tooltip that appears when hovering over speak button in footer. |
| `relTimeNow` | `'Now'`| The relative timestamp that's shown right after a new message |
| `relTimeMoment` | `'A few seconds ago'`| The relative timestamp that displays ten seconds after the message has been received and before 60 seconds has elapsed since the last message was received. |
| `relTimeMin` | `'{0}min ago'`| The relative timestamp that's shown for every minute since last message. The text {0} is replaced by the number of minutes passed . |
| `relTimeHr` | `'{0}hr ago'`| The relative timestamp shown for each hour since the last message. The text {0} is replaced by the number of hours passed. |
| `relTimeDay` | `'{0}d ago'`| The relative timestamp that's shown each day since last message. The text {0} is replaced by the number of days passed. |
| `relTimeMon` | `'{0}mth ago'`| The relative timestamp shown for each month since the last message. The text {0} is replaced by the number of months passed. |
| `relTimeYr` | `'{0}yr ago'`| The relative timestamp shown for every year since last message. The text {0} is replaced by the number of years passed. |
| `typingIndicator` | `'Waiting for response'` | The accessibility text for the typing indicator. It is spoken by the screen readers. |
| `upload` | `'Share popup'` | The tooltip that appears when hovering over upload share popup button in footer. |
| `uploadFailed` | `'Upload Failed.'` | The error text for an upload failure. |
| `uploadFileSizeLimitExceeded` | `'Upload Failed. File size should not be more than {0}MB.'` | The error text that's displayed when upload file size is too large. The text {0} is replaced by the SDK to the maximum allowed file size, which defaults to 25MB. |
| `uploadFileSizeZeroByte` | `'Upload Failed. Files of size zero bytes can\'t be uploaded.'` | The error text that's displayed when the upload file size is 0 bytes. |
| `uploadUnsupportedFileType` | `'Upload Failed. Unsupported file type.'` | The error text that's displayed when an unsupported file type upload is attempted. |
| `userMessage` | `'I say'` | The user message indicator for screen readers. It is spoken by the screen readers before the user messages. |
| `utteranceGeneric` | `'Message from skill.'` | The fallback description of a response message for an utterance that was not parsed by the SDK. |
| `webViewAccessibilityTitle` | `'In-widget WebView to display links'` | The default accessibility title for the WebView which is read out by screen readers |
| `webViewClose` | `'Done'` | The default label/tooltip title for WebView close button |
| `webViewErrorInfoDismiss` | `'Dismiss'` | The tooltip for the dismiss button in the fallback Snackbar inside WebView to close it |
| `webViewErrorInfoText` | `'Don’t see the page? {0}Click here{/0} to open it in a browser.'` | The informational text displayed in a Snackbar inside WebView as a fallback for the user in case the URL fails to load in the WebView. The text between {0} and {/0} is set to the original link that opens in a new tab or window. |

Here's an example of providing custom text in a few locales.
```js
i18n: {
    fr: {
        chatTitle: 'Soutien'
    },
    en: {
        chatTitle: 'Support'
    },
    es: {
        chatTitle: 'Apoyo'
    },
    'zh-cn': {
        chatTitle: '支持'
    }
}
```
If custom strings are provided for any locale other than 'en', all keys must be specified for that locale, otherwise 'en' translations are displayed for the missing values.

The settings can be configured as provided in the example below:
```html
<script>
var chatSettings = {
    URI: '<Chat server URI>',
    channelId: '<Channel ID>',
    userId: '<User ID>',
    fontFamily: '"Helvetica Neue", Helvetica, Arial, sans-serif',
    locale: 'en',
    enableClearMessage: true,
    botButtonIcon : 'style/Robot.png',
    botIcon: 'style/Robot.png',
    personIcon: 'style/userIcon.png'
};

function initSDK(name) {
    // If WebSDK is not available, reattempt later
    if (!WebSDK) {
        setTimeout(function() {
            initSDK(name);
        }, 2000);
        return;
    }

    // Default name is Bots
    if (!name) {
        name = 'Bots';
    }

    setTimeout(function() {
        var Bots = new WebSDK(chatSettings);    // Initiate library with configuration

        // Add ready listener before calling connect()
        // It is preferable to add other listeners before calling connect() too
        Bots.on('ready', function() {
            console.log('The widget is ready');
        });

        Bots.connect();     // Connect to server

        window[name] = Bots;
    }, 0);
}
</script>
<script src="<WebSDK URL>" onload="initSDK('<WebSDK namespace>')">
```

### Customizing CSS Classes

To further customize the look of the chat widget, its CSS classes can be overridden with custom style rules. Some main classes are as follows:

| class | Component |
| ------ | ------ |
| oda-chat-wrapper | Wrapper for entire chat widget |
| oda-chat-button | Collapsed chat widget button |
| oda-chat-notification-badge | Unseen message notification badge |
| oda-chat-widget | Expanded chat widget; wraps the widget header, conversation, and footer |
| oda-chat-header | Chat widget header |
| oda-chat-logo | Logo on the widget header |
| oda-chat-title | Title on the widget header |
| oda-chat-connection-status | Connection status. Each connection value has its own class as well - oda-chat-connected, oda-chat-disconnected etc. |
| oda-chat-connected | Applied as a sibling to connection-status when the widget is connected to server |
| oda-chat-connecting | Applied as a sibling to connection-status when the widget is connecting to server |
| oda-chat-disconnected | Applied as a sibling to connection-status when the widget is disconnected from server |
| oda-chat-closing | Applied as a sibling to connection-status when the widget is disconnecting from server |
| oda-chat-header-button | Common class for all header buttons |
| oda-chat-button-clear | Clear messages button |
| oda-chat-button-narration | Skill audio response toggle button |
| oda-chat-button-close | Close widget button |
| oda-chat-conversation | Container for the conversation |
| oda-chat-message | Common wrapper class for all chat messages |
| oda-chat-left | Skill message wrapper |
| oda-chat-right | User message wrapper |
| oda-chat-icon-wrapper | Skill/person icon wrapper displayed alongside message |
| oda-chat-message-icon | Skill/person icon image displayed alongside message |
| oda-chat-message-bubble | Message bubble |
| oda-chat-message-actions | Action buttons wrapper |
| oda-chat-message-global-actions | Global action buttons wrapper |
| oda-chat-action-postback | Postback action button |
| oda-chat-action-location | Location request action button |
| oda-chat-card | Card message |
| oda-chat-footer | Chat widget footer |
| oda-chat-footer-button | Common class for all footer buttons |
| oda-chat-button-upload | Upload file button |
| oda-chat-button-send | Send message button |
| oda-chat-user-input | User input textarea |

## Enums

The `WebSDK` object exposes various enums for the settings that support specific values. Once the library has been loaded, these enum values can be used to configure or update the SDK. The enums are:

### WebSDK.EVENT

This enum provides the event values that can be subscribed for using `Bots.on` method. The enum values are:
* CHAT_LANG - 'chatlanguagechange'
* CLICK_AUDIO_RESPONSE_TOGGLE - 'click:audiotoggle'
* CLICK_ERASE - 'click:erase'
* CLICK_VOICE_TOGGLE - 'click:voicetoggle'
* DESTROY - 'destroy'
* MESSAGE - 'message'
* MESSAGE_RECEIVED - 'message:received'
* MESSAGE_SENT - 'message:sent'
* NETWORK - 'networkstatuschange'
* READY - 'ready'
* TYPING - 'typing'
* UNREAD - 'unreadCount'
* WIDGET_CLOSED - 'widget:closed'
* WIDGET_OPENED - 'widget:opened'

The enum values can be passed to add a listener to the corresponding event, e.g. Bots.on(WebSDK.EVENT.MESSAGE_SENT, function() {}) to listen for sent messages. For details about each event, see [Events](#events).

### WebSDK.SPEECH_LOCALE

This enum provides the locales that are supported by the voice recognition service. The enum values are:
* DE_DE - 'de-de' - German
* EN_AU - 'en-au' - English (Australian)
* EN_GB - 'en-gb' - English (UK)
* EN_US - 'en-us' - English (US)
* ES_ES - 'es-es' - Spanish
* FR_FR - 'fr-fr' - French
* IT_IT - 'it-it' - Italian
* PT_BR - 'pt-br' - Portuguese (Brazilian)

The enum values can be passed in `speechLocale` setting, or `setSpeechLocale()` API.

### WebSDK.THEME

This enum provides the themes that can be applied to the chat widget. The values are:
* DEFAULT - 'default' - The default theme, provides contrast ratio between background layout and foreground text colors to meet [WCAG 2.1](https://www.w3.org/TR/WCAG21/) AAA requirements.
* REDWOOD_DARK - 'redwood-dark' - Redwood dark theme, provides contrast ratio between background layout and foreground text colors to meet WCAG 2.1 AA requirements.
* CLASSIC - 'classic' - The classic theme that used for prior versions of the widget. This theme does not meet the minimum color contrast between the background layout and foreground text colors as required by WCAG 2.1.


## Methods

The name that's passed in the `initSDK` parameter (WebSDK Namespace) will be used to invoke the SDK's public APIs. For example, if the name is set as `'Bots'`, the APIs can be invoked with `Bots.<API>()`.

### connect()

Connects to current chat server.

```js
Bots.connect()
```

The API returns a promise which can be used to execute code after connection is complete or closed.

```js
Bots.connect()
    .then(
        function() {
            // Successful connection
        },
        function(error) {
            // Something went wrong during connection
        }
    )
```

### connect(config)

Connects to current chat server with passed parameters. All fields are optional, if a field is not passed and is already set from initial settings or an earlier invocation, the existing value is reused. If `userId` is not passed and is not set so far, a random userId is generated and used.

```js
Bots.connect({
    URI: '<URI>',
    channelId: '<channelId>',
    userId: '<userId>'
})
```

The API returns a Promise which can be used to execute code after connection is complete or closed.

```js
Bots.connect({
    URI: '<URI>'
    channelId: '<channelId>',
    userId: '<userId>'})
    .then(
        function() {
            // Successful connection
        },
        function(error) {
            // Something went wrong during connection
        }
    )
```

The call to `connect()` API can result in a new connection or continuing existing connection depending on a few factors:
* On calling `connect()` with no parameters during no active connection, a new connection is initiated using the existing settings. For client auth enabled mode, a new token is fetched to open the connection.
* On calling `connect(param)` with parameters during no active connection, a new connection is initiated using the passed parameters. For client auth enabled mode, parameters other than `URI` are ignored, as the `channelId` and `userId` is parsed from the token.
* On calling `connect()` with no parameters during an active connection, the current connection is continued, and the returned Promise is immediately resolved.
* On calling `connect(params)` with parameters during an active connection in client auth disabled mode, if the passed parameters are same as existing parameters, the current connection is continued.
* On calling `connect(params)` with parameters during an active connection in client auth disabled mode, if the passed parameters are different from existing parameters, the current connection is closed and a new connection is initiated with passed parameters.
* On calling `connect(params)` with parameters during an active connection in client auth enabled mode, the current connection is closed and a new connection is initiated with a new token only if a new `URI` is passed in parameters. Otherwise, the current connection is continued.


### disconnect()

Closes currently active connection to the chat server. This includes the closing the connection to the chat server, any active voice recognition, ongoing attachment uploads, and running speech synthesis.

```js
Bots.disconnect()
```

The API returns a `Promise` which is resolved when the connection is closed.

```js
Bots.disconnect()
    .then(function() {
        console.log('The connection is now closed');
    });
```

### isConnected()

Returns whether the connection to the chat server is currently active.

```js
Bots.isConnected()
```


### openChat()

Opens the chat widget popup.

```js
Bots.openChat();
```

### closeChat()

Collapses the chat widget and displays the chat icon.

```js
Bots.closeChat();
```

### isChatOpened()

Returns true if the widget is open, otherwise false.

```js
Bots.isChatOpened();
```

### destroy()

Destroys the SDK instance by closing any active connection, voice recognition, speech synthesis, file uploads, and by removing the widget from the UI. Once called, none of the current instance methods can be called afterwards.

```js
Bots.destroy();
```

### sendAttachment(file)

Uploads file to the server. Returns a Promise that is resolved with the server response for successful uploads, or gets rejected with an error message for unsuccessful uploads.

```js
Bots.sendAttachment(file)
    .then(function(result) {
        console.log('File uploaded successfully.');
    })
    .catch(function(reason) {
        console.log(reason);
    });
```

### sendMessage(message, flags)

Sends a message on user’s behalf. Returns a Boolean to indicate whether the message was sent.

```js
Bots.sendMessage({
    type: 'text',
    text: 'hello'
});
// OR
Bots.sendMessage('hello');
```

The messages can be sent in three formats:

* passing text string
```js
Bots.sendMessage('Show my payslip')
```

You can also pass a location coordinates in a similar fashion:

```js
Bots.sendMessage('32.323232, 143.434343')   // Latitude, longitude
```

* passing messagePayload of message

```js
Bots.sendMessage({
    type: 'text',
    text: 'Show menu'
})

Bots.sendMessage({
    postback: {
        variables: {},
        'system.botId': '5409672A-AB06-4109-8303-318F5EDE91AA',
        action: 'pizza',
        'system.state': 'ShowMenu'
    },
    text: 'Order Pizza',
    type: 'postback'
})
```

* passing entire message

```js
Bots.sendMessage({
    messagePayload: {
        postback: {
            variables: {},
            system.botId: '5409672A-AB06-4109-8303-318F5EDE91AA',
            action: 'pizza',
            'system.state': 'ShowMenu'
        },
        text: 'Order Pizza',
        type: 'postback'
    },
    userId: 'Guest'
})
```

To keep the message from being displayed in the widget, pass the `hidden` Boolean flag in the flags object.

```js
Bots.sendMessage('What is the menu today?', { hidden: true });
```

The above call will send the message to server without displaying it in the widget.

### updateUser(userDetails)

Updates the user information.

```js
Bots.updateUser({
    messagePayload: {
        text: 'give me a pizza',
        type: 'text'
    },
    profile: {
        firstName: 'Jane',
        lastName: 'Smith',
        email: 'updated@email.com',
        properties: {
            justGotUpdated: true
        }
    }
});
```

Note: You also can use the `initUserProfile` property to set profile values. If you use the `initUserHiddenMessage` property, and the response from the server is expected to have user profile values, then you must use the `initUserProfile` property instead of setting the values in `updateUser()`. For later updates to user profile, you can continue using `updateUser()`.

### getSuggestions(query)

If autocomplete feature is enabled (`enableAutocomplete: true`), this API returns a `Promise` that resolves to the suggestions for the given query string. If it takes too long (~10s) to fetch the suggestion, the Promise is rejected.

```js
Bots.getSuggestions('pizza')
    .then(function(suggestions) {
        var suggestionString = suggestions.toString();
        console.log('The suggestions are: ', suggestionString);
    })
    .catch(function(reason) {
        console.log('Suggestion request failed', reason);
    });
```

The API expects a single query string parameter and returns a `Promise`. On a successful request for suggestions, the `Promise` is resolved to a string array. On failure, the `Promise` is rejected with an error message.

If the API is called when the feature is disabled, it returns a rejected Promise.

### startVoiceRecording(onSpeechRecognition, onSpeechNetworkChange, options)

Starts the voice recording if the speech recognition feature is enabled. The API returns a `Promise` that is resolved when the speech service is able to start recording. In case of an error, the `Promise` is rejected with an Error object.
The API expects two callbacks to be passed as its parameters:
`onSpeechRecognition` function is called on the speech server response. The JSON response is passed as parameter.
`onSpeechNetworkChange` function is called on change in the speech connection. A single parameter is passed - the WebSocket status.

```js
Bots.startVoiceRecording(function(data) {
    var recognizedText = '';
    if (data && (data.event === 'finalResult' || data.event === 'partialResult')) {
        if (data.nbest && data.nbest.length > 0) {
            recognizedText = data.nbest[0].utterance;
        }
    }
}, function(status) {
    if (status === WebSocket.OPEN) {
        // Connection established
    } else if (status === WebSocket.CLOSED) {
        // Connection closed
    }
})
```

The function additionally accepts an optional `options` object that can have fields for two callback functions for analyser - `onAnalyserReady`, and `onAnalyserFrequencies`. Either one, or both fields, can be passed.
These callbacks can be used to get regular frequency values for visualization.

`onAnalyserReady` is a one-time callback that is called when the analyser node is initialized. The callback method is passed as a single argument, an [`AnalyserNode`](https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode/), which is configured with an `fftSize` of 256, and connected to the voice input source.

`onAnalyserFrequencies` is a callback method that is called every time a new set of voice input frequencies are provided by the analyser node. The callback method is passed a single argument, an `Uint8Array` of size 128, depicting the frequency data composed of integers on a scale from 0 to 255. Each item in the array represents the decibel value for a specific frequency. The frequencies are spread linearly from 0 to 1/2 of the sample rate. For example, for 48000 sample rate, the last item of the array will represent the decibel value for 24000 Hz.

```js
Bots.startVoiceRecording(function(data) {
    var recognizedText = '';
    if (data && (data.event === 'finalResult' || data.event === 'partialResult')) {
        if (data.nbest && data.nbest.length > 0) {
            recognizedText = data.nbest[0].utterance;
        }
    }
}, function(status) {
    if (status === WebSocket.OPEN) {
        // Connection established
    } else if (status === WebSocket.CLOSED) {
        // Connection closed
    }
}, {
    onAnalyserReady: function(analyserNode) { console.log('The analyser node is', analyserNode); },
    onAnalyserFrequencies: function(frequencies) { console.log('New input frequencies are', frequencies); }
})
```

### stopVoiceRecording()

Stops any running voice recording. Throws an error if speech recognition is not enabled.

```js
Bots.stopVoiceRecording()
```

### setSpeechLocale(locale)

Sets the locale used for speech connection. The user is expected to speak with the same locale that is set here to the SDK. The locales currently supported are `'en-us'`, `'fr-fr'`, `'es-es'`, and `'pt-br'`. If an unsupported locale is passed, the API returns `false` while maintaining the passed locale. In such case, any voice recognition attempt is failed.
The function returns a Boolean indicating whether the passed locale is supported or not.

```js
Bots.setSpeechLocale('fr-fr');
```

> **Note**: When both voice recognition and audio response are enabled but the audio response locale is not set, then the locale for the audio response voice gets set to the same locale as the voice recognition locale.

Example:
```js
var Bots = new WebSDK({
    // ...,
    enableSpeech: true,
    enableBotAudioResponse: true
});

// ...

Bots.setSpeechLocale('es-es');

```

In above example, the locale for audio response voice is set to `'es-es'` automatically.

### setPrimaryLanguage(languageTag)

Updates the language selected for the conversation between the user and the skill in the selection dropdown. This function can only be called when multi-lingual chat feature is configured.

```js
Bots.setPrimaryLanguage('fr')
```

If the passed language tag does not match any of the passed supported languages, 'Detect Language' is set and skill determines which language is being used for conversation.

### setSkillVoices(voices)

Dynamically updates the synthesis voice used to narrate skill messages. The function can accept a single skillVoice object or an array of skillVoice objects. The function returns a `Promise` which resolves to the skill voice that is applied to the synthesis service. It can be one of the passed voices or a fallback in case none of the passed voice is available on device. The `Promise` is rejected if the skill audio response feature is not enabled.


```js
Bots.setSkillVoices({ lang: 'fr-fr' });

Bots.setSkillVoices({ lang: 'fr-fr', name: 'Thomas' })

Bots.setSkillVoices([{
    lang: 'es-mx',
    name: 'Juan'
}, {
    lang: 'es-es',
    name: 'Monica'
}, {
    lang: 'es-ar',
    name: 'Diego'
}, {
    lang: 'es-es'
}])
```


### setDelegate(delegate)

The `setDelegate` method can be used to change or remove delegate callbacks after a conversation has been initialized. If no value is passed, the existing delegates are removed.

```js
Bots.connect().then(function() {
    Bots.setDelegate({
        beforeDisplay(message) {
            return message;
        },
        beforeSend(message) {
            return message;
        },
        beforePostbackSend(postback) {
            return postback;
        }
    })
});
```

### getConversationHistory()

Returns information about current conversation for the user. The response is an object containing user ID, messages, and unread message count.

```js
Bots.getConversationHistory()

{
    messages: [
        {
            date: '2020-01-22T17:06:24.085Z',
            isRead: true,
            messagePayload: {
                text: 'show menu',
                type: 'text'
            },
            userId: 'user74882436'
        }
    ],
    messageCount: 1,
    unread: 0,
    userId: 'user74882436'
}
```

### clearConversationHistory(userId, shouldClearWidget)

This API clears the conversation history for a known user from the browser's localStorage. The `userId` must be a string. On passing empty or no userId, current user's history is removed.

If the passed `userId` is same as current user's `userId`, then you can also pass an optional boolean argument, `shouldClearWidget`, to configure whether the current chat widget UI should also be cleared on calling this API. By default, the value is `true`.

*Note* - This API does not interact with `sessionStorage` for users other than current user. The `sessionStorage` is automatically cleared on closing the tab.

```js
Bots.clearConversationHistory('Jonathan');      // Removes conversation history of Jonathan

Bots.clearConversationHistory('Adriana');       // Removes conversation history of Adriana and clears the widget UI if Adriana is current user

Bots.clearConversationHistory('', false);       // Removes conversation history of current user without clearing the widget UI
```

### clearAllConversationsHistory(shouldClearWidget)

This API clears the conversation history for all users from the browser's localStorage. Like `clearConversationHistory`, this method can also help in recovering significant portions of localStorage from the user's browser.

You can also pass an optional boolean argument, `shouldClearWidget`, to configure whether the current chat widget UI should also be cleared on calling this API. By default, the value is `true`.

**Warning** - The actions taken by calling this API can not be undone. Once the messages are deleted, they cannot be recovered. Call this method sparingly and only when absolutely needed.

*Note* - This API does not interact with `sessionStorage` for users other than current user. The `sessionStorage` is automatically cleared on closing the tab.

```js
Bots.clearAllConversationsHistory()
```

### getUnreadMessagesCount()

Returns the count of the unread messages.

```js
Bots.getUnreadMessagesCount();
```

### setAllMessagesAsRead()

Marks all messages as have been read/seen by user.

```js
Bots.getUnreadMessagesCount(); // 2
Bots.setAllMessagesAsRead();
Bots.getUnreadMessagesCount(); // 0
```

### setUserInputMessage(text)

Fills user input field with passed message.

```js
Bots.setUserInputMessage('Show my agenda for today please.');
```

### setUserInputPlaceholder(text)

Updates user input's placeholder text. It can be utilized to change the placeholder text according to the input expected from the user.

```js
Bots.setUserInputPlaceholder('Add your pizza topping');
```

### showTypingIndicator()

Displays the typing indicator in the conversation. If the typing indicator is already visible, the timer to hide it gets reset. The typing indicator is automatically removed if the server sends a response, or the timer period set by `typingIndicatorTimeout` (in seconds) is expired.

The method only works if `showTypingIndicator` setting is set `true`, the SDK is not being used in headless mode, and the widget is connected to the server.

```js
Bots.showTypingIndicator();
```


### setWebViewConfig(webViewConfig)

Sets and updates the WebView configuration, customizing the WebView component. Check out In-Widget WebView section under customizations for more details.

```js
Bots.setWebViewConfig({
    accessibilityTitle: 'WebView container for Wikipedia',
    sandbox: ['allow-scripts', 'allow-downloads']
    size: 'tall',
    title: 'Wikipedia'
});
```

### setChatBubbleIconHeight(height)

Sets the height of loading chat bubble icon. The height must be provided as a string value in one of standard [length](https://developer.mozilla.org/en-US/docs/Web/CSS/length) units.

```js
Bots.setChatBubbleIconHeight('18px');
```

### setChatBubbleIconWidth(width)

Sets the width of loading chat bubble icon. The width must be provided as a string value in one of standard [length](https://developer.mozilla.org/en-US/docs/Web/CSS/length) units.

```js
Bots.setChatBubbleIconWidth('24px');
```

### setChatBubbleIconSize(width, height)

Sets the size of loading chat bubble icon. The width and height must be provided as string values in one of the standard [length](https://developer.mozilla.org/en-US/docs/Web/CSS/length) units.

```js
Bots.setChatBubbleIconSize('24px', '18px');
```

### setFont(font)

Sets the font for the chat widget. The syntax of `font` must follow the [standard pattern](https://developer.mozilla.org/en-US/docs/Web/CSS/font).

```js
Bots.setFont('14px italic large sans-serif');
```

> Note: The function has been made obsolete and will be removed in upcoming releases. Plesae use `setFontFamily()` for setting font family, and `setFontSize()` for setting font size.

### setFontFamily(fontFamily)

Set font family used for all text content in the chat widget. The `fontFamily` argument must be a string and follow the [standard pattern](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family).

```js
Bots.setFontFamily('"Gill Sans", sans-serif');
```

### setFontSize(fontSize)

Sets the font size for the text in chat widget. The syntax of `fontSize` must follow the standard [permissible values](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size).

```js
Bots.setFontSize('16px');
```

### setHeight(height)

Sets the height of chat widget. The value passed must be in one of [length](https://developer.mozilla.org/en-US/docs/Web/CSS/length) units.

```js
Bots.setHeight('786px')
```

### setWidth(width)

Sets the width of chat widget. The value passed must be in one of [length](https://developer.mozilla.org/en-US/docs/Web/CSS/length) units.

```js
Bots.setWidth('320px')
```

### setSize(width, height)

Sets the size of chat widget. The values passed must be in one of [length](https://developer.mozilla.org/en-US/docs/Web/CSS/length) units.

```js
Bots.setSize('320px' ,'786px',)
```

### setMessagePadding(padding)

Sets the padding around the message in the chat widget. The syntax of `padding` must follow standard [permissible values](https://developer.mozilla.org/en-US/docs/Web/CSS/padding).

```js
// Apply padding to all four sides
Bots.setMessagePadding('15px');
// vertical | horizontal
Bots.setMessagePadding('5% 10%');
// top | horizontal | bottom
Bots.setMessagePadding('15em 20em 20em');
// top | right | bottom | left
Bots.setMessagePadding('15px 20px 20px 15px');
```

### setTextColor(color)

Sets the primary text color of messages in chat widget. It does not modify the colors in actions. The value passed must be in standard [color](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value) format.

```js
Bots.setTextColor('#33ee00')
```

### setTextColorLight(color)

Sets the color of the secondary messages in chat widget, like descriptions. The value passed must be in standard [color](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value) format.

```js
Bots.setTextColorLight('rgb(13, 155, 200)')
```


## Events

To bind an event, use `Bots.on(<event name>, <handler>)`. To unbind events, you can either:
* Call `Bots.off(<event name>, handler)` to remove one specific handler.
* Call `Bots.off(<event name>)` to remove all handlers for an event.
* Call `Bots.off()` to unbind all handlers.

It is preferable to add event handlers before calling `connect()` method, so that they can be registered and triggered appropriately.

### ready

This event is triggered when init completes successfully. Be sure to bind before calling init.

```js
Bots.on('ready', function(){
    console.log('the init has completed!');
});
```

Listeners to `ready` event must be added before calling the `connect()` method, otherwise the listeners will not be registered in time to be triggered.

### destroy

This event is triggered when the widget is destroyed.
```js
Bots.on('destroy', function(){
    console.log('the widget is destroyed!');
});
Bots.destroy();
```

### message:received

This event is triggered when the user receives a message.
```js
Bots.on('message:received', function(message) {
    console.log('the user received a message', message);
});
```

### message:sent

This event is triggered when the user sends a message.
```js
Bots.on('message:sent', function(message) {
    console.log('the user sent a message', message);
});
```

### message

This event is triggered when a message was added to the conversation.
```js
Bots.on('message', function(message) {
    console.log('a message was added to the conversation', message);
});
```

### networkstatuschange

This event is triggered whenever the network status of the connection to the server changes. The callback receives a status number parameter, which corresponds to [WebSocket network status constants](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket#Constants).
```js
Bots.on('networkstatuschange', function(status) {
    switch (status) {
        case 0:
            status = 'Connecting';
            break;
        case 1:
            status = 'Open';
            break;
        case 2:
            status = 'Closing';
            break;
        case 3:
            status = 'Closed';
            break;
    }
    console.log(status);
});
```

### typing

This event is triggered whenever the user starts or stops typing in the user input field. The listener receives a boolean parameter, which is set `true` when user starts typing and set `false` when user stops typing.
```js
Bots.on('typing', function(isTyping) {
    console.log('User currently typing: ', isTyping);
});
```

### unreadCount

This event is triggered when the number of unread messages changes.
```js
Bots.on('unreadCount', function(unreadCount) {
    console.log('the number of unread messages was updated', unreadCount);
});
```

### widget:opened

This event is triggered when the widget is opened.
```js
Bots.on('widget:opened', function() {
    console.log('Widget is opened!');
});
```

### widget:closed

This event is triggered when the widget is closed.
```js
Bots.on('widget:closed', function() {
    console.log('Widget is closed!');
});
```

### click:audiotoggle

This event is triggered when the audio utterance of response is toggled. The subscribers receive the Boolean status - `true` if the audio response is turned on, `false` if it is turned off.
```js
Bots.on('click:audiotoggle', function(status) {
    if (status === true) {
        console.log('Audio response is turned on.');
    } else {
        console.log('Audio response is turned off.');
    }
})
```

### click:erase

This event is triggered when the erase conversation history button is clicked. No parameters are passed to the subscribers.
```js
Bots.on('click:erase', function() {
    console.log('Conversation history is erased.');
})
```

### click:voicetoggle

This event is triggered when the voice activation button is toggled. The subscribers receive the Boolean status - `true` if the voice is activated, `false` if it is deactivated.
```js
Bots.on('click:voicetoggle', function(status) {
    if (status === true) {
        console.log('Voice recording is started.');
    } else {
        console.log('Voice recording is stopped.');
    }
})
```

### chatlanguagechange

This event is triggered when the chat language in language selection dropdown is selected or changed. This dropdown is exposed on enabling [Multi-Lingual Chat](#multi-lingual-chat) feature. Its subscribers receive the selected language's language tag. If auto-detect is selected, `null` is passed as the argument.


```js
Bots.on('chatlanguagechange', function(language) {
    console.log('The selected chat language is', language);
});
```


## Features

### Autocomplete

`Feature Flag: enableAutocomplete: true` (default: `false`)

`Enable client side caching: enableAutocompleteClientCache`

Autocomplete provides suggestions to end users to better form the utterance and select the specific entity value. For it to work, you must add autocomplete suggestions to the skill's intents. Then, whenever the user types a character in the input, the intents' autocomplete suggestions display in a popup to suggest the best format and to minimize user errors. An intent's autocomplete suggestions should not be a full word dictionary. Their purpose is to minimize the scope and allow better guidance to the end user.

The feature can also be used in headless mode using `getSuggestions()` API. The API details are described in the Method section above.

### Delegation

`Feature configuration: delegate`

The delegation feature lets you set a delegate to receive callbacks before certain events in the conversation. To set a delegate, pass it in the `delegate` property or use the `setDelegate` method. The delegate object may optionally contain `beforeDisplay`, `beforeSend`, and `beforePostbackSend` delegate functions.

```js
var delegate = {
    beforeDisplay: function(message) {
        return message;
    },
    beforeSend: function(message) {
        return message;
    },
    beforePostbackSend: function(postback) {
        return postback;
    }
}

Bots.setDelegate(delegate);
```

#### beforeDisplay

The `beforeDisplay` delegate allows a skill message to be modified before it is displayed in the conversation. The message returned by the delegate is used to display the message. If it returns a falsy value, like `null`, `undefined`, or `false`, the message is not displayed.

#### beforeSend

The `beforeSend` delegate allows a user message to be modified before it is sent to the chat server. The message returned by the delegate is sent to skill. If it returns a falsy value, like `null`, `undefined`, or `false`, the message is not displayed.

#### beforePostbackSend

The `beforePostbackSend` delegate is similar to `beforeSend`, just applied to postback messages from user. The postback returned by the delegate is sent to skill. If it returns a falsy value, like `null`, `undefined`, or `false`, the message is not displayed.


### Embedded mode

`Feature flag: embedded: true` (default: `false`)

`Pass ID of target container element: targetElement`

The chat widget appears as a fixed position element on the bottom right of the page, which does not respond to gestures on the page. But it can also be embedded into the host and become part of the page. To activate the embedded mode, you need to pass `embedded: true`, and provide a target container with `targetElement: <targetDivId>` . This accepts a DOM element which will be used as the container where the widget will be rendered.

The embedded widget occupies the full width and height of the container. A height and width must be specified for the target element. Otherwise, the widget will collapse.


### Headless SDK

`Feature flag: enableHeadless: true` (default: `false`)

Similar to headless browsers, the SDK can also be used without a UI. The SDK maintains the connection to the server, and provides APIs to send messages, receive messages, and get updates of the to network status. Developers can use the APIs to interact with the SDK, and update UI appropriately.

The communication can be implemented as follows:
* Sending messages - Call `Bots.sendMessage(message)` to pass any payload to server.
* Receiving messages - Response can be listened for using `Bots.on('message:received', <messageReceivedCallbackFunction>)`.
* Get connection status update - Updates to status of the connection to server can be listened for using `Bots.on('networkstatuschange', <networkStatusCallbackFunction>)`. The callback has a parameter `status`, which is updated with values from 0 to 3. These values map to [WebSocket states](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket#Constants):
  * 0 - WebSocket.CONNECTING - Connecting
  * 1 - WebSocket.OPEN - Open
  * 2 - WebSocket.CLOSING - Closing
  * 3 - WebSocket.CLOSED - Closed
* Check if connection is open - Call `Bots.isConnected()` to check if the connection is open or not.
* Get suggestions list - If autocomplete is enabled, call `Bots.getSuggestions(query)` where query is the string to get the suggestions list.


### In-Widget WebView

Feature flag: `linkHandler: { target: 'oda-chat-webview' }`

Customization: `webViewConfig`

Public method: `setWebViewConfig(webViewConfig)`

The Web SDK contains an In-widget WebView component that can be used to view the message links within the chat widget. This feature allows users to interact with links in the conversation without taking them away from the widget to a new tab or window. The in-widget WebView can be applied globally to open all links in the messages inside it, or can be selectively configured for specific links.

To open all links in the conversation in the WebView, you just need to pass `linkHandler: { target: 'oda-chat-webview' }` in the settings. This sets the target of all links to 'oda-chat-webview', which is the WebView iframe's name.

In more general scenarios, you'll probably need to open only certain links in the WebView, while ensuring other links open normally in other tabs/windows. The `beforeDisplay` delegate can be used to make that work. To open a specific message URL action in the WebView, replace action.type field's value from 'url' to 'webview'. Once the action type is changed to 'webview' in beforeDisplay, clicking that action button will open the link in the WebView.
Opening specific links embedded in the text in WebView is a bit more challenging. The embedded link needs to be converted into anchor element (\<a href="https://www.oracle.com"\>), and `target="oda-chat-webview"` attribute should be added in that anchor element.

The `webViewConfig` setting allows customizing the WebView component. It accepts an object that can have following optional fields:
```js
{
    accessibilityTitle: string,                             // Name of WebView frame element for Web Accessibility
    closeButtonIcon: string,                                // Image URL/SVG string that is used to display the close button icon
    closeButtonLabel: string,                               // Text label/tooltip title for the close button
    closeButtonType: 'icon' | 'label' | 'iconWithLabel',    // Sets how the close button is displayed in the WebView
    errorInfoBar: boolean,                                  // Sets to display or hide fallback view with original URL
    errorInfoDismissLabel: string,                          // Label for error-view bar dismiss button
    errorInfoText: string,                                  // Informational text displayed in an error-view bar inside WebView as a fallback for the user in case the URL fails to load in the WebView
    referrerPolicy: ReferrerPolicy                          // Indicates which referrer to send when fetching the frame's resource
    sandbox: string[],                                      // Array of extra restrictions to the content in the WebView frame
    size: 'tall' | 'full',                                  // Height of the WebView compared to chat widget. When set 'tall', it is set as 80%, 100% for 'full'.
    title: string                                           // WebView title shown on the header of the WebView container
}
```

The `referrerPolicy` policy value passed should be a [valid directive](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy#Directives). The default policy applied is `'no-referrer-when-downgrade'`.

The `sandbox` field accepts array of valid restriction strings that allows for the exclusion of certain actions inside the frame. The restrictions that can be passed to the field can be found under the sandbox attribute manual at [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe).

The configuration can also by updated dynamically by passing a webViewConfig object in the method `setWebViewConfig()`. Every property in the object is optional.

The WebView optionally presents a fallback Snackbar view that contains the original URL link as a fallback in case the page fails to load inside the WebView. Clicking the link in this view opens the page in a new tab. The informational text can be customized with `webViewErrorInfoText` i18n translation string, and must contain a placeholder text for for the link label. e.g.
```js
settings = {
    URI: 'instance',
    //...,
    i18n: {
        en: {
            webViewErrorInfoText: 'This link can\'t be opened here. You can open it in a new page by clicking {0}here{/0}.'
        }
    }
}
```
This error view can be disabled by passing `errorInfoBar: false` in the `webViewConfig` setting.

**Limitations**
1. Pages which provide response header `X-frame-options: deny` or `X-frame-options: sameorigin` may not open in the WebView due to server side restrictions preventing the page to be opened inside iframes. The WebView presents the link back to the user in a dissmissable Snackbar in the WebView and they can open it in a new window or tab by clicking it.
2. Due to the above restrictions, authorization pages like IDCS, Google Login, FB Login etc. can not be opened inside the WebViews, as authorization pages always return `X-frame-options: deny` to prevent [clickjacking](https://tools.ietf.org/html/draft-ietf-oauth-v2-23#section-10.13).
3. Only links inside the conversation messages can be opened inside the WebView. Any external links must not be targeted to be opened in the WebView, clicking on such links won't open the WebView correctly.


### Long Polling

`Feature flag: enableLongPolling: true` (default: `false`)

The SDK uses WebSockets to connect to the server and converse with skills. If for some reason the WebSocket is disabled over the network, traditional http calls can be used to chat with the skill. This feature is known as long polling, as the SDK has to continuously call or 'poll' the server to fetch the latest messages from the skill.

Long polling provides fallback support for conversations on browsers which don't have WebSockets enabled or blocked.


### Multi-Lingual Chat

`Feature flag: multiLangChat`

The Web SDK's native language support enables the chat widget to both detect a user's language and allow the user to select a preferred language from a dropdown menu in the header. Users can switch languages between conversations, not during conversations.

To enable this menu, define the `multiLangChat` property with an object containing the `supportedLangs` array, which is comprised of language tags (`lang`) and an optional display label (`label`). Outside of this array, you can optionally set the default language with the `primary` key.

```js
multiLangChat: {
    supportedLangs: [{
        lang: 'en'
    }, {
        lang: 'es',
        label: 'Español'
    }, {
        lang: 'fr',
        label: 'Français'
    }, {
        lang: 'hi',
        label: 'हिंदी'
    }],
    primary: 'en'
}
```

The chat widget shows the passed supported languages in a dropdown menu in the header. On selecting a language, the current conversation is reset, and a new conversation is started with the selected language. If the response narration feature is enabled, the responses are narrated in the selected language's voice. If the voice recognition feature is enabled, and a language supported by the recognition service is selected, it also uses the same language to interpret user's voice messages.

The chat widget additionally displays a 'Detect Language' option in the dropdown. Selecting this tells the skill to automatically detect the conversation language from the user's message and respond in the same language, if possible.

You can dynamically update the selected language by calling `setPrimaryChatLanguage(lang)` API. If the passed lang matches one of the supported languages, it is selected. On finding no match, 'Detect Language' is selected. You can also select 'Detected Language' option by calling `setPrimaryChatLanguage('und')`, where `'und'` indicates undetermined.

The language selected by a given user persists across sessions in the same browser. When the same user revisits the page with the chat widget with same skill, the previously selected language is automatically selected.

You can add listener for a change in the selected language with `'chatlanguagechange'` event. The syntax of adding listener to this event is provided at [chatlanguagechange](#chatlanguagechange) event section.

Here are some things to keep in mind:
* You need to define a minimum of two languages to enable this dropdown menu to display.
* The `label` key is optional for the natively supported languages: `fr` displays as 'French' in the menu, `es` displays as 'Spanish', and so on. However, if you've added a language that's not one of the natively supported languages, then you should add a `label` to identify the tag, especially when there is no `i18n` string for the language. For example, if you don’t define `label: 'हिंदी'` , for the `lang: hi`, then the dropdown displays 'hi' instead, contributing to a suboptimal user experience.
* Labels for the languages can be set more dynamically by passing the labels in `i18n` setting. You can set the label for any language by passing it to its `language_<languageTag>` key. For example,
```js
i18n: {
    en: {
        langauge_de: 'German',
        language_en: 'English',
        language_sw: 'Swahili',
        language_tr: 'Turkish'
    },
    de: {
        langauge_de: 'Deutsche',
        language_en: 'Englisch',
        language_sw: 'Swahili',
        language_tr: 'Türkisch'
    }
}
```
This pattern allows setting labels for any language, supported or unsupported, and also allows translations of the label itself in different locales.
* If you omit the `primary` key, the widget automatically detects the language in the user profile and selects the Detect Language option in the menu.
* Voice recognition and narration, when configured, are available when users select a supported language, but are not available when the Detect Language option is set.
* If voice recognition is enabled, selecting a language that is not supported by the voice recognition disables the recognition functionality until a supported language is selected.


### Response narration

`Feature flag: enableBotAudioResponse: true` (default: `false`)

`Functionality configuration: skillVoices`

The SDK can use the device's speech synthesis APIs to narrate the server's responses. You use the `skillVoices` array to set the voice preferences. Each item in the array must be an object that has a `lang` field and an optional `name` field. The SDK looks up the availability of each voice on the device in the order that they are passed in the setting, and the first complete match is set as the voice. If no exact match is found, then the SDK uses the first match based on the `lang` value alone. If there's still no match, then the SDK uses the device's default language.

```js
var settings = {
    ...,
    enableBotAudioResponse: true,
    skillVoices: [{
        lang: 'en-US',
        name: 'Samantha'
    }, {
        lang: 'en-US',
        name: 'Alex'
    }, {
        lang: 'en-UK'
    }]
}
```

With version 21.02, the `skillVoices` array allows passing additional `pitch`, `rate`, and `volume` optional properties in each item to tailor the way the utterances are spoken. These properties correspond to the same fields in [SpeechSynthesisUtterance](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisUtterance) interface.

The `pitch` property can have a value between 0 and 2, `rate` can have a value between 0.1 and 10, and `volume` can have a value between 0 and 1.

```js
var settings = {
    // ....,
    skillVoices: [{
        lang: 'en-us',
        name: 'Alex',
        pitch: 1.5,
        rate: 2,
        volume: 0.8
    }, {
        lang: 'en-us',
        name: 'Victoria',
        pitch: 1.2,
        rate: 1.7,
    }, {
        lang: 'en',
        name: 'Fiona',
        pitch: 2,
    }, {
        lang: 'en'
    }]
}
```

### Voice Recognition

`Feature flag: enableSpeech: true` (default: `false`)

`Functionality configuration: enableSpeechAutoSend`

The SDK has been integrated with speech recognition to send messages in the form of voice to skills and digital assistants. It allows users to talk directly to the skill during conversations and get appropriate responses.

When the feature is enabled, a mic button appears in place of the send button whenever the user input field is empty. The user can click on the mic button to start voice recording and send it to the speech server for recognition. The speech is converted to text and sent to the skill or digital assistant. If the speech is partially recognized, the partial result is set in the user input field and the user can clean it up before sending it.

The feature can also be utilized using two exposed methods - `startVoiceRecording(onSpeechRecognition, onSpeechNetworkChange, options)` to start recording, and `stopVoiceRecording()` to stop recording. The APIs are detailed in the Method section above.

The `enableSpeechAutoSend` flag setting lets you configure whether to send the text that's recognized from the user's voice directly to the chat server. When set to `true` (the default), the user's speech response is automatically sent to the chat server. When set to `false`, the user's speech response is rendered in the input text field before it is sent to the chat server so that users can manually modify it before sending, or delete the message.


### Absolute and Relative Timestamps

Feature flag: `enableTimestamp: true` (default: `true`)

Functionality configuration: `timestampFormat`

You can enable absolute or relative timestamps for chat messages. Absolute timestamps display the exact time for each message. Relative timestamps display only on the latest message and express the time in terms of the moments, minutes, hours, days, months, or years ago relative to the previous message.

The precision afforded by absolute timestamps make them ideal for archival tasks, but within the limited context of a chat session, this precision detracts from the user experience because users must compare timestamps to find out the passage of time between messages. Relative timestamps allow users to track the conversation easily through terms like *Just Now* and *A few moments ago* that can be immediately understood. Relative timestamps improve the user experience in another way while also simplifying your development tasks: because relative timestamps mark the messages in terms of seconds, minutes, hours, days, months, or years ago, you don't need to convert them for time zones.


## Customizations

Customizability is one of the biggest strengths of the Web SDK. In this section, we'll cover some of the various customizations that can be performed on the SDK.

### Add avatar icons with messages

The messages in the chat are by default not accompanied with any avatars. It can however be configured to show icons with user and skill messages with the help of following parameters:
* `botIcon` - URL of the image source that should be displayed alongside the skill messages. e.g. botIcon: 'https://image.flaticon.com/icons/svg/3011/3011301.svg'
* `personIcon` - URL of the image source that should be displayed alongside the user messages, e.g. personIcon: 'https://image.flaticon.com/icons/svg/3011/3011311.svg'
Additionally, if the skill has a live agent integration, the SDK can be configured to show a different icon for agent messages.
* agentAvatar - URL of the image source that should be displayed alongside the agent messages. If this value is not provided, but botIcon is set, botIcon is used instead.

All of the above settings can only be passed in the initialization settings, and can not be modified dynamically.

### Change header buttons icons

There are three buttons on the chat header that be displayed in the chat widget. These buttons can be configured and customized as follows:

* Clear Message button - Clicking this button clears the current and older messages in the conversation
    * Feature flag - `enableClearMessage: true`
    * Custom icon - `clearMessageIcon: '<image URL | SVG string>'`
* Audio response toggle button - This button toggles the utterance of skill responses as they are received. As it is a toggle button, it has two states, utterance on, where responses are spoken, and utterance off, where responses are not spoken.
    * Feature flag - `enableBotAudioResponse: true`
    * Custom icon - response on - `audioResponseOnIcon: '<image URL | SVG string>'`
                    response off - `audioResponseOffIcon: '<image URL | SVG string>'`
* Close widget button - This button collapses the widget and shows the launch button. This button can not be disabled in normal chat widget, and it is not shown in the embedded chat widget.
    * Feature flag - none (always enabled in chat widget, not displayed in embedded mode)
    * Custom icon - `closeIcon : '<image URL | SVG string>'`

These header button icons can customized in two ways - by passing the source URL of the image, or by passing a raw SVG string. If raw SVG string is passed, the fill color of the SVG can be customized by CSS classes, as well as by passing a color value in colors.headerButtonFill property in initial settings. The color customization may not work for all SVGs, as they can be multi-colored or have their own stroke and fill colors.

### Draggable launch button

Feature flag: `enableDraggableButton: true` (default: `false`)

In some scenarios, the chat widget launch button can block the background content and there may not be an easy way to view it. This can be especially apparent in mobile screens where there is less space available for the web page. However, by setting `enableDraggableButton` to `true`, the chat widget launch button can be made draggable, so the users can drag it around the screen as needed. This flag only affects the launch button. The widget still gets expanded from its original location.

### Focus first action of skill message

Feature flag: `focusOnNewMessage: 'action'` (default: `'input'`)

With each new message, the chat widget normally sets the focus back to the user input field. This works well when the dialog flow expects a lot of textual input from the user. However, if the dialog flow contains a number of messages with actions, then the user need to either employ their mouse or reverse tab navigation to select one of the actions. For such use cases and for power users who prefer keyboard based navigation, a better choice can be focusing the first action button in the skill message as it is received. By setting `focusOnNewMessage: 'action'`, when a new skill message containing actions is received, the focus is set to the first action button. If the message does not contain any actions, the focus is set to the user input field.

### Format message timestamps

Feature flag: `enableTimestamp: true` (default: `true`)

Functionality configuration: `timestampFormat`

Timestamps are shown with messages indicating the time they were sent or received. By default, they are displayed in the locale time in day of week, month date, year, time am/pm format, e.g. Thursday, August 13, 2020, 9:52:22 AM. This timestamp can be configured by passing formatting options in the `timestampFormat` setting.

The formatting can be performed in two ways - by passing a pattern string consisting of formatting tokens, or by passing an object containing [Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#Syntax) options.

* Using pattern string
The timestamp can be formatted by passing a pattern string which is composed of format tokens. The available format tokens are:

| Component | Token | Output |
| --------- | ----- | ------ |
| Day of Month | D | 1 2 ... 30 31 |
|| Do | 1st 2nd ... 30th 31st |
|| DD | 01 02 ... 30 31 |
| Day of Week | d | 0 1 ... 5 6 |
|| ddd | Sun Mon ... Fri Sat |
|| dddd | Sunday Monday ... Friday Saturday |
| Month | M | 1 2 ... 11 12 |
|| MM | 01 02 ... 11 12 |
|| MMM | Jan Feb ... Nov Dec |
|| MMMM | January February ... November December |
| Year | YY | 70 71 ... 29 30 |
|| YYYY | 1970 1971 ... 2029 2030 |
| Hour | H | 0 1 ... 22 23 |
|| HH | 00 01 ... 22 23 |
|| h | 1 2 ... 11 12 |
|| hh | 01 02 ... 11 12 |
| Minute | m | 0 1 ... 58 59 |
|| mm | 00 01 ... 58 59 |
| Second | s | 0 1 ... 58 59 |
|| ss | 00 01 ... 58 59 |
| Fractional Second | S | 0 1 ... 8 9 |
|| SS | 0 1 ... 98 99 |
|| SSS | 0 1 ... 998 999 |
|AM/PM | A | AM PM |
|| a | am pm |
| Timezone | Z | -07:00 -06:00 ... +06:00 +07:00 |
|| ZZ | -0700 -0600 ... +0600 +0700 |

So, passing timestampFormat: `'hh:mm:ss a'` would set timestamp as '09:30:14 pm'.

**NOTE** - The tokens in the pattern string are case-sensitive, e.g. passing yyyy instead of YYYY would not show year in the date.

* Using Intl.DateTimeFormat options object

The timestamp can also be formatted using the options defined for [Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#Syntax) object. The object can be passed with some or all of the following properties:

| Property | Acceptable Values |
| -------- | ----------------- |
| dateStyle | 'full', 'long', 'medium', 'short' |
| timeStyle | 'full', 'long', 'medium', 'short' |
| weekday | 'long' (e.g., Thursday), 'short' (e.g., Thu), 'narrow' (e.g., T) |
| day | 'numeric' (e.g., 1), '2-digit' (e.g., 01) |
| month | 'numeric' (e.g., 2), '2-digit' (e.g., 02), 'long' (e.g., March), 'short' (e.g., Mar), 'narrow' (e.g., M) |
| year | 'numeric' (e.g., 2012), '2-digit' (e.g., 12) |
| era | 'long' (e.g., Anno Domini), 'short' (e.g., AD), 'narrow' (e.g., A) |
| hour | 'numeric', '2-digit' |
| minute | 'numeric', '2-digit' |
| second | 'numeric', '2-digit' |
| timeZoneName |  'long' (e.g., British Summer Time), 'short' (e.g., GMT+1) |
| timeZone | The time zone to use. The only value implementations must recognize is "UTC"; the default is the runtime's default time zone. Implementations may also recognize the time zone names of the IANA time zone database, such as "Asia/Shanghai", "Asia/Kolkata", "America/New_York". |
| hour12 | Whether to use 12-hour time (as opposed to 24-hour time). Possible values are `true` and `false` |

### Opening Links

Custom handling: `linkHandler: { onclick: <function>, target: '<string>' }`

In In-widget WebView : `linkHandler: { target: 'oda-chat-webview' }`

In new window: `openLinksInNewWindow: true`

The Web SDK provides various ways for you to control the target location of the URL links within the conversations. By default, clicking any link in the conversation opens the linked URL in the same page. You can configure the widget to open it in a specific target using `linkHandler` setting.

The `linkHandler` setting expects an object that can take two optional fields - `target` and `onclick`. The `target` field accepts a string which identifies the location where the linked URL is to be displayed (a tab, window, or \<iframe\>). he following keywords have special meanings for where to load the URL:
* `'_self'`: the current browsing context.
* `'_blank'`: usually a new tab, but users can configure browsers to open a new window instead.
* `'_parent'`: the parent browsing context of the current one. If no parent, behaves as `'_self'`.
* `'_top'`: the topmost browsing context (the "highest" context that’s an ancestor of the current one). If no ancestors, behaves as `'_self'`.

```js
settings = {
    ...,
    linkHandler: { target: '_blank'}
};

var Bots = new WebSDK(settings);
```

To open the links inside an iframe, you can pass its name attribute in the target property.

```html
<iframe name="container" width="400" height="300"></iframe>

<script>
  settings = {
      ...
      linkHandler: { target: 'container'}
  }

  var Bots = new WebSDK(settings);
</script>
```

The `onclick` property of `linkHandler` allows you to add an event listener on all anchor links in the conversation. The listener is fired before the link is opened, and can be used to perform actions based on the link. The listener is passed an `event` object as parameter which is generated by the click action. You can prevent the link from being opened by returning `false` from the listener. The listener is also bind to the anchor element which is clicked, and the `this` context referes to the `HTMLAnchorElement` inside the listener.

```js
linkHandler: {
    onclick: function(event) {
        console.log('The element clicked is', this);
        console.log('The event fired from the click is', event);
        console.log('The clicked link is', event.target.href);
        console.log('Preventing the link from being opened');
        return false;
    }
}
```
You can set either one or both properties of the `linkHandler` setting, but passing one of the fields is required.

In some scenarios, you may want to open links explicitly in a new window, overriding browser preferences. This can be achieved by passing `openLinksInNewWindow: true` in the settings.

Finally, the chat widget also provides an in-widget WebView which can be used to display linked URLs inside the widget. This helps in preventing the user from navigating away from the page to a new tab or window. See [In-Widget WebView](#in-widget-webview) for more details on this feature.

### Relative Timestamps

Feature flag: `timestampMode: 'relative'`

Timestamp color: `colors.timestamp: 'color string'`

The appearance of the message timestamps can be modified with the `timestampMode` setting. When set `'relative'`, the timestamp is only shown before the first message of the day as a header, and for the new messages as an updating timestamp indicating the time passed since the message was added in the conversation. This relative timestamp is refreshed in following intervals if no new message is added:
* For first 10s
* Between 10s-60s
* Every minute between 1m-60m
* Every hour between 1hr-24hr
* Every day between 1d-30d
* Every month between 1m-12m
* Every year after first year

As soon as a new message is added to the conversation, the relative timestamp from last message is removed, and added to the new message. The timestamp is also updated to start afresh for the new message.

For older messages in the conversation, a timestamp header is shown indicating the date before the first message of the day, for all days a conversation is performed. The timestamp header format can be customized using the `timestampFormat` setting.

### Restrict attachment types

`Feature flag: enableAttachment: true` (default: `true`)

`Functionality configuration: shareMenuItems`

Users can share various kinds of files and their location to the skills using the share menu from the chat widget. By default, the share attachment popup menu shows 4 items - sharing visual media files i.e. images and videos, audio files, general files like documents, pdf, excel sheets etc., and location. This menu can be customized to show fewer options using the `shareMenuItems` setting. This setting accepts an array of strings where each item maps to a menu item – `'visual'` for **Share Image/Video**, `'audio'` for **Share Audio**, `'file'` for **Share File**, and `'location'` for **Share Location**. The share menu only shows the items for passed values, so by passing fewer items, the share menu can be modified, e.g. passing `shareMenuItems: ['audio', 'location']` in the settings will only show the `Share Audio` and `Share Location` menu items in the share popup menu. However, passing an empty array, or invalid values will show all menu items. To show no items, the feature can be disabled by passing `enableAttachment: false`.

#### Custom share menu items

Starting with 21.04, the Web SDK also allows configuring share menu items to set specific file types that users are allowed to upload. The custom menu item can be passed as an object to `shareMenuItems` array. It can be passed along with the string categories, or can also be passed without them. A custom share menu item may look as follows:
```js
{
    type: string,       // Space separated list of file formats, pass '*' to allow all supported filie types

    label: string,      // OPTIONAL, label for the share menu item, should preferably be configured through i18n strings

    icon?: string,      // OPTIONAL, Icon image source path or SVG source string, the file icon is displayed as fallback

    maxSize?: number    // OPTIONAL, Maximum file size allowed for upload in KiloBytes, the maximum and fallback value is 25 MB (25600 KB)
}
```

Following code snippet shows passing custom menu items in settings and defining their labels using `i18n` field.

```js
var settings = {
    shareMenuItems: [ {
        type: 'odf',
        label: 'Upload ODF',
    }, {
        type: 'pdf'
    }, {
        type: 'jpg png jpeg',
        icon: 'https://image-source-site/imageicon'
    }, {
        type: 'doc docx xls',
        maxSize: 4096
    }],
    i18n: {
        en: {
            share_pdf: 'Upload PDF',
            share_jpg_png_jpeg: 'Upload Image',
            share_doc_docx_xls: 'Upload document'
        }
    }
}
```
As seen in the example above, the `i18n` labels for the custom menu items can be set by passing them with `share_\<type joined by '_'\>` keys. For the wildcard '*', the label can be set using `'share_all'` i18n key. Using `i18n` is recommended over `label` as it allows supporting the menu item labels in multiple languages.

Using attachment functionality often requires updating the network security policy of the host site. The attachments are uploaded to ODA object storage using HTTP calls, and may get blocked by the site's [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) policies. With the site blocking the uploads, an error can be seen in browser console indicating that the client has blocked the request due to CORS policy. To fix such issues, the network security policy of the host site should be updated to whitelist the ODA domain, allowing the upload requests to go through.
Since the CORS policy does not apply to WebSockets, the conversations between the SDK and ODA skills are not impacted by such restrictions.

When connecting to a client auth enabled channel on ODA platform running Version 20.12 and above, you can optionally make attachments more secure by passing `enableAttachmentSecurity: true`. When set to `true`, extra headers are passed to the attachment upload requests to ensure that they can't be downloaded without passing a valid signed JWT token as value of `token` query parameter in the attachment fetch request URL.

> **Note**: Do not enable this setting if the skill connects to an ODA instance that's Version 20.08 or runs on any version prior to 20.08. This property only applies to client auth-enabled connections to Versions 20.12 and higher of the ODA platform.


## Message Model

To use features like headless mode and delegate, a clear understanding of skill and user messages is essential. Everything received from and sent to the chat server are represented as messages. This includes:
* Messages from user → skill (e.g. "I want to order a Pizza")
* Messages from skill → user (e.g. "What kind of crust do you want?")

The following section describes each of the message types in more detail.

### Base Types
These are the base types that are used by User → Skill messages and Skill → User messages. They are the building blocks for the messages.


#### Action
An action represents something that the user can select. Every action includes the following properties:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | Action type for the action | string | Yes |
| label | Label to display for the action | string | At least one of `label` or `imageUrl` must be present |
| imageUrl | Image to display for the action | string | At least one of `label` or `imageUrl` must be present |


##### PostbackAction
This action will send a pre-defined postback back to the skill if the user selects the action.
It adds the following properties to the `Action` properties:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | Action type for the action | "postback" | Yes |
| postback | The postback to be sent back if the action is selected | string or JSONObject | Yes |

Example JSON
```json
{
    "type": "postback",
    "label": "Large Pizza",
    "imageUrl": "https://amicis.com/images/gallery/locations/11.jpg",
    "postback": {
        "state": "askSize",
        "action": "getCrust"
    }
}
```


##### CallAction
This action will request the client to call a specified phone number on the user's behalf.
It adds the following properties to the `Action` properties:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | Action type for the action | "call" | Yes |
| phoneNumber | The phone number to call | string | Yes |

Example JSON
```json
{
    "type": "call",
    "label": "Call Support",
    "imageUrl": "http://ahoraescuando.bluefm.com.ar/files/2016/05/cuidado.jpg",
    "phoneNumber": "18002231711"
}
```


##### UrlAction
This action will request the client to open a website in a new tab or in an in-app browser.
It adds the following properties to the `Action` properties:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | Action type for the action | "url" | Yes |
| URL | The URL of the website to display | string | Yes |


##### ShareAction
This action will request the client to open a sharing dialog for the user.
It adds the following properties to the `Action` properties:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | Action type for the action | "share" | Yes |


##### LocationAction
This action will request the client to ask the user for a location.
It adds the following properties to the `Action` properties:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | Action type for the action | "location" | Yes |

Example JSON
```json
{
    "type": "location",
    "label": "Share location",
    "imageUrl": "http://images.clipartpanda.com/location-clipart-location-pin-clipart-1.jpg"
}
```


#### Attachment
This represents an attachment sent User → Skill or Skill → User.

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| title | A title for the attachment | string | No |
| type | The type of attachment | string (valid values: 'audio', 'file', 'image', 'video') | Yes |
| URL | The URL to download the attachment | string | Yes |

Example JSON
```json
{
    "title": "Oracle Open World Promotion",
    "type": "image",
    "URL": "https://www.oracle.com/us/assets/hp07-oow17-promo-02-3737849.jpg"
}
```


#### Card
A card represents a single card in the message payload.  It contains the following properties:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| title | The title of the card, displayed as the first line on the card. | string | Yes |
| description | The description of the card | string | No |
| imageUrl | URL of the image that is displayed | string | No |
| URL | URL of a website that is opened when taping on the card | string | No |
| actions | An array of actions related to the text | Array<Action> | No |


#### Location
This represents a Location object.

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| title | A title for the location | string | No |
| URL | A URL for displaying a map of the location | string | No |
| latitude | The GPS coordinate's longitude value | double | Yes |
| longitude | The GPS coordinate's longitude value | double | Yes |

Example JSON
```json
{
    "title": "Oracle Headquarters",
    "URL": "https://www.google.com.au/maps/place/37°31'47.3%22N+122°15'57.6%22W",
    "longitude": -122.265987,
    "latitude": 37.529818
}
```


### Conversation Messages
All messages that are part of the conversation are structured as follows:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| messagePayload | Message payload | Message | Yes |
| userId | User ID | string | Yes |

Example conversation message
```json
{
    "messagePayload": {
        "text": "show menu",
        "type": "text"
    },
    "userId": "guest"
}
```


### Message
Message is the abstract base type for all other messages. All messages extend it to provide more information.

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | string | Yes |


### User Message
This represents a Message sent from user → skill.


#### User Text Message
This is a simple text message sent to the server.
It applies the following properties to the Message:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | "text" | Yes |
| text | Text message | string | Yes |

```json
{
    "messagePayload": {
        "text": "Order Pizza",
        "type": "text"
    },
    "userId": "guest"
}
```


#### User Attachment Message
This is the attachment response message sent to the server.
It applies the following properties to the Message:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | "attachment" | Yes |
| attachment | Attachment metadata | Attachment | Yes |

```json
{
    "messagePayload": {
        "attachment": {
            "type": "image",
            "URL": "http://oda-instance.com/attachment/v1/attachments/d43fd051-02cf-4c62-a422-313979eb9d55"
        },
        "type": "attachment"
    },
    "userId": "guest"
}
```


#### User Location Message
This is the location response message sent to the server.
It applies the following properties to the Message:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | "location" | Yes |
| location | User location information | Location | Yes |

```json
{
    "messagePayload": {
        "location": {
            "latitude": 45.9285271,
            "longitude": 132.6101925
        },
        "type": "location"
    },
    "userId": "guest"
}
```


#### User Postback Message
This is the postback response message sent to the server.
It applies the following properties to the Message:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | "postback" | Yes |
| text | Text for postback | string | No |
| postback | The postback of the selected action | string or JSONObject | Yes |

```json
{
    "messagePayload": {
        "postback": {
            "variables": {
                "pizza": "Small"
            },
            "system.botId": "69F2D6BB-35BF-4BCA-99A0-A88D44A51B35",
            "system.state": "orderPizza"
        },
        "text": "Small",
        "type": "postback"
    },
    "userId": "guest"
}
```


### Skill Message
This represents a Message sent from Skill → User.


#### Skill Text Message
This represents a text message.
It applies the following properties to the Message:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | "text" | Yes |
| text | Text of the message | string | Yes |
| actions | An array of actions related to the text | Array<Action> | No |
| globalActions | An array of global actions related to the text | Array<Action> | No |

```json
{
    "messagePayload": {
        "type": "text",
        "text": "What do you want to do?",
        "actions": [
            {
                "type": "postback",
                "label": "Order Pizza",
                "postback": {
                    "state": "askAction",
                    "action": "orderPizza"
                }
            },
            {
                "type": "postback",
                "label": "Cancel A Previous Order",
                "postback": {
                    "state": "askAction",
                    "action": "cancelOrder"
                }
            }
        ]
    },
    "userId": "guest"
}
```


#### Skill Attachment Message
This represents an attachment message.
It applies the following properties to the Message:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | "attachment" | Yes |
| attachment | The attachment sent | Attachment | Yes |
| actions | An array of actions related to the text | Array<Action> | No |
| globalActions | An array of global actions related to the text | Array<Action> | No |


#### Skill Location Message
This represents a location message.
It applies the following properties to the Message:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | "location" | Yes |
| location | The location | Location | Yes |
| actions | An array of actions related to the text | Array<Action> | No |
| globalActions | An array of global actions related to the text | Array<Action> | No |


#### Skill Postback Message
This represents a postback.
It applies the following properties to the Message:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | "postback" | Yes |
| text | Text of the message | string | No |
| postback | The postback | string or JSONObject | Yes |
| actions | An array of actions related to the text | Array<Action> | No |
| globalActions | An array of global actions related to the text | Array<Action> | No |


#### Skill Card Message
This represents a set of choices displayed to the user, either horizontally like a carousal or vertically like a list.
It applies the following properties to the Message:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | "card" | Yes |
| layout | Whether to display the cards horizontally or vertically | string (values: horizontal, vertical) | Yes |
| cards | Array of cards to be rendered | Array<Card> | Yes |
| headerText | A header text for cards | string | No |
| actions | An array of actions related to the text | Array<Action> | No |
| globalActions | An array of global actions related to the text | Array<Action> | No |

Example JSON
```json
{
    "messagePayload": {
        "type": "card",
        "layout": "horizontal",
        "cards": [
            {
                "title": "Hawaiian Pizza",
                "description": "Ham and pineapple on thin crust",
                "actions": [
                    {
                        "type": "postback",
                        "label": "Order Small",
                        "postback": {
                            "state": "GetOrder",
                            "variables": {
                                "pizzaType": "hawaiian",
                                "pizzaCrust": "thin",
                                "pizzaSize": "small"
                            }
                        }
                    },
                    {
                        "type": "postback",
                        "label": "Order Large",
                        "postback": {
                            "state": "GetOrder",
                            "variables": {
                                "pizzaType": "hawaiian",
                                "pizzaCrust": "thin",
                                "pizzaSize": "large"
                            }
                        }
                    }
                ]
            },
            {
                "title": "Cheese Pizza",
                "description": "Cheese pizza (i.e. pizza with NO toppings) on thick crust",
                "actions": [
                    {
                        "type": "postback",
                        "label": "Order Small",
                        "postback": {
                            "state": "GetOrder",
                            "variables": {
                                "pizzaType": "cheese",
                                "pizzaCrust": "thick",
                                "pizzaSize": "small"
                            }
                        }
                    },
                    {
                        "type": "postback",
                        "label": "Order Large",
                        "postback": {
                            "state": "GetOrder",
                            "variables": {
                                "pizzaType": "cheese",
                                "pizzaCrust": "thick",
                                "pizzaSize": "large"
                            }
                        }
                    }
                ]
            }
        ],
        "globalActions": [
            {
                "type": "call",
                "label": "Call for Help",
                "phoneNumber": "123456789"
            }
        ]
    },
    "userId": "guest"
}
```


#### Skill Raw Message
This is used when a component creates the channel-specific payload itself.
It applies the following properties to the Message:

| Name | Description | Type | Required |
| ------ | ------ | ------ | ------ |
| type | The message type | "raw" | Yes |
| payload | The channel-specific payload | JSONObject | Yes |


## Limitations

There are a few limitations on the usage of current Web SDK.

* The skill's may start sending incorrect messages if the network goes offline for a short time during a chat (such as 10 seconds) before going back online. This only happens when a server response is lost due to a network failure. In such cases, the user may have to send the previous message again, or may need to start the conversation afresh. The skill can be designed to handle such cases.
* The attachment file size is limited to 25 MB. Larger files cannot be uploaded in this release.
* The SDK currently only supports a single connection to the ODA instance per userId per browser or device. If multiple connections are made using the same userId from several devices, or from multiple browsers on single device, then only the responses from the skill and digital assistant will be synchronized on all clients, not the user messages.
