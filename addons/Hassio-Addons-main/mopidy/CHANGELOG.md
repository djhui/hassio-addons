## 2.2.0 - 2022-08-07

* 🔼 Update alpine to `3.16`
* 🔼 Update Mopidy to `3.3.0-r0`
* 🔼 Update Mopidy-Iris to `3.64.1`
* 🔼 Update Mopidy-MPD to `3.3.0`
* 🔼 Update python3 to `3.10.5-r0`
* 🔼 Update py3-gst to `1.20.3-r0`
* 🔼 Update py3-pip to `22.1.1-r0`
* 🔼 Update ca-certificates to `20220614-r0`
* 🔼 Update sudo to `1.9.10-r0`
* 🔨 Migrated to S6-Overlay `V3`
* 📝 Updated to new repository structure + Yaml config


## 2.1.1 - 2022-04-11

* 🐛 Fix alpine package repositories
* ➖ Removed fixed tornado version


## 2.1.0 - 2022-04-05

* 🔼 Update alpine to `3.14`
* 🔼 Update Mopidy-Iris to `3.62.0`
* 🔼 Update Mopidy-MPD to `3.2.0`
* 🔼 Update python3 to `3.9.5-r2`
* 🔼 Update ca-certificates to `20211220-r0`
* 🔼 Update sudo to `1.9.7_p1-r1`
* 📝 Updated config.json and Readme


## 2.0.1 - 2020-06-03

* 🔼 Update python3 to `3.9.5-r1`
* 🐛 Specifiy own S6 entrypoint, don't rely on the base image.


## 2.0.0 - 2020-05-02

* ✨ Resurrect Mopidy
* 🔼 Update Mopidy to `3.1.1-r3`
* 🔨 Use Alpine as base image
* 🔨 Migrate to new `devices` option format. Thanks @LiJu09

### ⚠️ Breaking Change ⚠️

When coming from a previous version validate your settings, since the addon got completly redone!


## 1.2.3 - 2020-05-22

* 🔨 Updated Changelog to new format
* 🕸️ Marked as deprecated


## 1.2.2 - 2020-02-09

### Changed

* 🔨 Start mopidy as `system` startup


## 1.2.1 - 2020-02-07

* 🔽 Downgrade Mopidy to `2.2.2-1`
* 🔼 Use mopidy-youtube `2.1.0`
* 🔼 Update youtube-dl to `2020.1.24`


## 1.2.0 - 2019-12-06

* ➕ Use Youtube-Mopidy integration from [@natumbri](https://github.com/natumbri/mopidy-youtube)
* 🔼 Updated Mopidy to `2.3.1-1`
* 🔼 Updated youtube-dl to `2019.11.28`
* 🔼 Update certifi to same version as youtube-dl
* 🔨 More startup logging


## 1.1.0 - 2019-10-19

* 🔼 Updated OS to debian buster (thanks @Nickerchen)
* ➖ Removed aarch64 support


## 1.0.0 - 2019-10-16

* 🔨 Set mopidy version to `2.1.0-1`
* ➕ Own versioning starting with 1.0.0
* ➕ Added example config setting for media dir
* 🐛 Fixed ALSA not forwarding sound correctly


## 2.2.3 - 2019-10-06 (old versioning)

* ➕ Put mopidy 2.2.3-1 inside the addon.
* 🔨 Added device mapping for `/dev/snd`
* 🔨 Adjust mopidy version for aarch64 systems. It will be the version `2.1.0-1` on those systems.
