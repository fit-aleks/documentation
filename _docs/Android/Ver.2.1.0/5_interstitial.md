---
title: "Request interstitial ad"
permalink: ver_2.1.0_5_interstitial.html
sidebar: mps_side_bar
---
You can also display interstitial ads to your MPSPage, very similarly to the way you added a banner ad.

You will continue expanding the MPSPage instance that you created earlier. To request an interstitial ad we add the following code to the java file.

```java
page.getInterstitialAd("testinterstitial", context, new MPSInterstitialAdListener() {
    @Override
    public void onAdLoaded(@NonNull MPSInterstitialAd mpsInterstitialAd) {
        super.onAdLoaded(mpsInterstitialAd);
        interstitialAd = mpsInterstitialAd;
        mpsInterstitialAd.present();
    }
});
```

Also you can pass additional ad targeting as second parameter to `getInterstitialAd` function:

```java
Map<String, String> additionalTargeting = new HashMap<>();
additionalTargeting.put("key", "value");
page.getInterstitialAd("testinterstitial", additionalTargeting, context, new MPSInterstitialAdListener() {
    @Override
    public void onAdLoaded(@NonNull MPSInterstitialAd mpsInterstitialAd) {
        super.onAdLoaded(mpsInterstitialAd);
        interstitialAd = mpsInterstitialAd;
        mpsInterstitialAd.present();
    }
});
```

Build and run the application.

## Result

This image shows the displayed banner ad.

![Interstitial Ad](/images/android/interstitial.png)
