---
title: "Project Setup"
permalink: ios_ver_1.1.4_project_setup.html
sidebar: mps_side_bar
---

## Prerequisites
* Xcode 8 or higher
* Deployment target of 8.0 or higher

<p id="download">
    <a  href="https://github.com/NBCUOTS/mobile_mps_sdk_ios_examples/releases/tag/release-1.0.0">Download MPS SDK Examples
    </a>
</p>

## 1.1 Create a New Project 

Open Xcode.  
Navigate to *File > New > Project...*  
Select *Single View Application* under iOS Applications, and click Next.

{% include image.html file="ios/Single_view_application.png" caption="" %}

Give your project the desired *Product Name*. For the purposes of this example we will call it ReferenceTestApp.  
Enter your *Organization Name* and *Identifier*.  
Choose either "Swift" or "Objective-C" for the *Language*. We will use Swift for this demo.  
Click Next.

{% include image.html file="ios/xcode_installation_name.png" caption="" %}

Finally create save the project in your desired location.

## 1.2 Add SDK to Your Project and Instantiate

Copy the provided **nbcu_mps_ios_sdk.framework** and **GoogleMobileAds.framework** to your project, and make sure the *Copy items if needed* and *Add to targets* options are enabled. Also add the **AdSupport.framework** to your projects Linked Frameworks and Libraries section.

{% include image.html file="ios/installation_step_1.png" caption="" %}

If you see a message about updating the Google Mobile Ads SDK, please contact the MPS SDK Support team prior to updating.  
Email: <mps-sdk-support@nbcuni.com>, DPIM Slack channel:  #mps_sdk_support

## 1.3 Add SDK to Embedded Framework

Add the **nbcu_mps_ios_sdk.framework** to the Embedded Binaries section of your project.

{% include image.html file="ios/embedded_framework.png" caption="" %}

## 1.4 Update App Transport Security in iOS 9

Google Mobile Ads SDK requires adding the **NSAllowsArbitraryLoads** exception to make sure your ads are not impacted by App Transport Security (ATS) on iOS 9 devices.   
For iOS 10 devices, **NSAllowsArbitraryLoadsForMedia** and **NSAllowsArbitraryLoadsInWebContent** are required to make sure your ads are not impacted by ATS.

Add these values to the **info.plist** file of your application. 

```
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```
Reference: [Google ATS details](https://developers.google.com/mobile-ads-sdk/docs/dfp/ios/app-transport-security). 

## 1.5 Objective-C Project Settings

For Objective-C projects you should enable swift libraries.

{% include image.html file="ios/project_stgs_objcs.png" caption="" %}

## 1.6 Update Simulator Scheme Environment Variables (optional)

If you want to disable system log messages, you can optionally add **OS_ACTIVITY_MODE=disable** to the *Environment Variables* under *Arguments* of the scheme.

{% include image.html file="ios/install_turn_off_notitifcations.png" caption="" %}

## 1.7 App Store Submission

Because the SDK is FAT Binary and works for simulators and devices you need to update it before App Store submission.

``` 
chmod u+x app-store-submission.sh
```

And add app-store-submission.sh file to run phases with

``` 
"$SRCROOT/PATH_TO_FILE/app-store-submission.sh"
``` 

{% include image.html file="ios/app-store-phases.png" caption="" %}

<style>
#download > a
{
    background-color: #039be5;
    color: #fff;
    box-shadow: 0 2px 5px 0 rgba(0,0,0,.26);  
    border: 0;
    border-radius: 2px;
    cursor: pointer;
    display: inline-block;
    height: 44px;
    margin: 0;
    min-width: 36px;
    outline: 0;
    padding: 8px;
    padding-left: 16px;
    padding-right: 16px;
    vertical-align: middle;
    text-align: center;
    vertical-align: middle;
}
</style>