# -*- coding: utf-8 -*-
# Deployment settings for MarmaladeAmazonAd.
# This file is autogenerated by the mkb system and used by the s3e deployment
# tool during the build process.

config = {}
cmdline = ['/Applications/Marmalade.app/Contents/s3e/makefile_builder/mkb.py', '/Users/adriangomez/OneDrive/Development/MarmaladeAmazonAd/MarmaladeAmazonAd.mkb', '--buildenv=XCODE', '--deploy-only']
mkb = '/Users/adriangomez/OneDrive/Development/MarmaladeAmazonAd/MarmaladeAmazonAd.mkb'
mkf = ['/Applications/Marmalade.app/Contents/s3e/s3e-default.mkf', '/Applications/Marmalade.app/Contents/modules/iwutil/iwutil.mkf', '/Applications/Marmalade.app/Contents/modules/third_party/libjpeg/libjpeg.mkf', '/Applications/Marmalade.app/Contents/modules/third_party/libpng/libpng.mkf', '/Applications/Marmalade.app/Contents/modules/third_party/zlib/zlib.mkf', '/Applications/Marmalade.app/Contents/modules/iwgl/iwgl.mkf', '/Applications/Marmalade.app/Contents/modules/third_party/cocos2dx/cocos2dx/proj.marmalade/cocos2dx.mkf', '/Applications/Marmalade.app/Contents/modules/third_party/cocos2dx/cocos2dx/platform/third_party/marmalade/libxml2.mkf', '/Applications/Marmalade.app/Contents/modules/third_party/cocos2dx/cocos2dx/platform/third_party/marmalade/freetype.mkf', '/Applications/Marmalade.app/Contents/modules/third_party/cocos2dx/cocos2dx/platform/third_party/marmalade/libtiff/libtiff.mkf', '/Applications/Marmalade.app/Contents/modules/third_party/cocos2dx/external/Box2D/proj.marmalade/Box2D.mkf', '/Applications/Marmalade.app/Contents/extensions/s3eAmazonAds/s3eAmazonAds.mkf']

class DeployConfig(object):
    pass

######### ASSET GROUPS #############

assets = {}

assets['Default'] = [
    ('/Users/adriangomez/OneDrive/Development/MarmaladeAmazonAd/data', '.', 0),
]

######### DEFAULT CONFIG #############

class DefaultConfig(DeployConfig):
    embed_icf = -1
    name = 'MarmaladeAmazonAd'
    pub_sign_key = 0
    priv_sign_key = 0
    caption = 'MarmaladeAmazonAd'
    long_caption = 'MarmaladeAmazonAd'
    version = [0, 0, 1]
    config = ['/Users/adriangomez/OneDrive/Development/MarmaladeAmazonAd/data/app.icf']
    data_dir = '/Users/adriangomez/OneDrive/Development/MarmaladeAmazonAd/data'
    iphone_link_lib = ['s3eAmazonAds']
    osx_ext_dll = []
    wp81_extra_pri = []
    ws8_ext_capabilities = []
    android_external_res = []
    win32_ext_dll = []
    wp8_ext_capabilities = []
    ws81_ext_managed_dll = []
    iphone_link_libdir = ['/Applications/Marmalade.app/Contents/extensions/s3eAmazonAds/lib/iphone']
    wp81_ext_capabilities = []
    android_extra_application_manifest = ['/Applications/Marmalade.app/Contents/extensions/s3eAmazonAds/source/android/ExtraAppManifests.xml']
    ws8_ext_native_dll = []
    android_external_assets = []
    blackberry_extra_descriptor = []
    ws8_extra_res = []
    android_extra_manifest = []
    wp81_ext_sdk_ref = []
    iphone_link_libdirs = []
    wp81_ext_device_capabilities = []
    linux_ext_lib = []
    ws8_ext_managed_dll = []
    ws8_ext_sdk_manifest_part = []
    ws8_ext_device_capabilities = []
    ws81_extra_pri = []
    android_external_jars = ['/Applications/Marmalade.app/Contents/extensions/s3eAmazonAds/lib/android/s3eAmazonAds.jar', '/Applications/Marmalade.app/Contents/extensions/s3eAmazonAds/third_party/amazon-ads-android-sdk/lib/amazon-ads-5.4.78.jar']
    win8_winrt_extra_res = []
    wp81_ext_sdk_manifest_part = []
    android_supports_gl_texture = []
    wp81_extra_res = []
    wp81_ext_managed_dll = []
    ws81_ext_sdk_manifest_part = []
    ws81_ext_device_capabilities = []
    ws8_ext_sdk_ref = []
    iphone_extra_string = []
    tizen_so = []
    wp8_ext_native_dll = []
    win8_phone_extra_res = []
    win8_store_extra_res = []
    iphone_link_opts = ['$MARMALADE_ROOT/extensions/S3eAmazonAds/third_party/amazon-ads-ios-sdk/AmazonAd', '-weak_framework AdSupport -weak_framework CoreLocation -weak_framework SystemConfiguration', '-weak_framework CoreTelephony -weak_framework MediaPlayer']
    ws81_ext_sdk_ref = []
    wp8_extra_res = []
    ws81_ext_native_dll = []
    ws8_extra_pri = []
    wp8_ext_managed_dll = []
    android_so = ['/Applications/Marmalade.app/Contents/extensions/s3eAmazonAds/lib/android/libs3eAmazonAds.so']
    wp8_ext_sdk_ref = []
    osx_extra_res = []
    ws81_extra_res = []
    wp81_ext_native_dll = []
    ws81_ext_capabilities = []
    iphone_link_libs = []
    target = {
         'x86' : {
                   'debug'   : r'/Users/adriangomez/OneDrive/Development/MarmaladeAmazonAd/build_marmaladeamazonad_xcode/build/Debug/MarmaladeAmazonAd.s86',
                   'release' : r'/Users/adriangomez/OneDrive/Development/MarmaladeAmazonAd/build_marmaladeamazonad_xcode/build/Release/MarmaladeAmazonAd.s86',
                 },
         'arm_gcc' : {
                   'debug'   : r'/Users/adriangomez/OneDrive/Development/MarmaladeAmazonAd/build_marmaladeamazonad_xcode/build/Debug ARM/MarmaladeAmazonAd.s3e',
                   'release' : r'/Users/adriangomez/OneDrive/Development/MarmaladeAmazonAd/build_marmaladeamazonad_xcode/build/Release ARM/MarmaladeAmazonAd.s3e',
                 },
        }
    arm_arch = ''
    assets_original = assets
    assets = assets['Default']

default = DefaultConfig()
