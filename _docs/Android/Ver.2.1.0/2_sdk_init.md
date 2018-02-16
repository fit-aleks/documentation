---
title: "Initiate the SDK"
permalink: ver_2.1.0_2_sdk_init.html
sidebar: jekyllhowto
---
You can now create an instance of MPS with the appropriate host URL and site by initializing the library. You can also specify the log level for this instance. Refer to MPSSDKLogLevel in the documentation for more details.

Before start using the SDK it should be created with the following method call. Non-null instance of context should be passed to initialize cache folders in app internal folder.

You can also set test mode. When this mode is set to true all MPS requests will pass additional field to indicate the test mode is activated.

```java
URL mpsUrl;
try {
    mpsUrl = new URL("https://mps.nbcuni.com");
} catch (MalformedURLException e) {
    Log.e(LOG_TAG, e.getLocalizedMessage(), e);
    return;
}

final MPSOptions options = new MPSOptions();
options.logLevel = MPSSDKLogLevel.DEBUG;
options.testMode = false;
final MPS mps = MPS.init(applicationInstance, mpsUrl, "test-sdk", options);
```

The last parameter can be one of the @MPSSDKLogLevel.LogLevel and defines the number of logs which will be printed by the SDK

## Request an MPSPage Object

The MPS library operates with the concept of an MPSPage, which is similar to one web page. You will use this MPSPage object to request ads.

To achieve this we create an instance of MPSPageParameters which facilitates building the request that will be sent to MPS. The list of all configurable properties are presented in the library documentation.

For example:

```java
final MPSPageParameters mpp = new MPSPageParameters(this, "some_path")
	.setCat("someCatValue")
	.addCag("someKey", "value");
final MpsPage page = mps.requestPageObject(mpp);
```

Next we will work on requesting banner and interstital ads, and adding them to the view hierarchy.