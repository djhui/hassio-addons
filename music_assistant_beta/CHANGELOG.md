# [2.5.0 BETA 10] - 09.03.2025

## What’s Changed

### Server 2.5.0 BETA 10

## What's Changed

* Tidal provider maintenance: add tidaluser class by @jozefKruszynski in https://github.com/music-assistant/server/pull/2010
* Fix Subsonic: Use transcode metadata when present by @khers in https://github.com/music-assistant/server/pull/2011
* Add pkce to Tidal provider's manifest requirements by @jozefKruszynski in https://github.com/music-assistant/server/pull/2013
* Add ListenBrainz scrobbler provider by @ijc in https://github.com/music-assistant/server/pull/2008
* Rename the slimproto provider to squeezelite by @marcelveldt in https://github.com/music-assistant/server/pull/2015
* Add Built-in (web) Player Provider by @maximmaxim345 in https://github.com/music-assistant/server/pull/2009
* Fix: Subsonic: Catch DataNotFoundError for artwork by @khers in https://github.com/music-assistant/server/pull/2012
* frontend-2.13.0 by @music-assistant-machine in https://github.com/music-assistant/server/pull/2016
* Various small bufixes


**Full Changelog**: https://github.com/music-assistant/server/compare/2.5.0b9...2.5.0b10

### Frontend 2.13.0

## 🐛 Bugfixes

- #903 - fix: Missing options when adding a new PEQ band (@maximmaxim345)

## 🚀 Features

- #901 - Allow RTSP URLs for Builtin Provider (@jdelaney72)
- #902 - Feat: Built-in Web Player Provider (@maximmaxim345)

## ⬆️ Dependencies

### Server

### Frontend



# [2.5.0 BETA 9] - 07.03.2025

## What's Changed

* Add LastFM Audio Scrobbler plugin provider by @wjzijderveld in https://github.com/music-assistant/server/pull/1850
* Fix broken links in DEVELOPMENT.md by @jdelaney72 in https://github.com/music-assistant/server/pull/2006
* Fix: Missing `MULTI_DEVICE_DSP` in player groups by @maximmaxim345 in https://github.com/music-assistant/server/pull/2007
* Add advanced networking (list of IPs) to Sonos S1 provider by @mcblum in https://github.com/music-assistant/server/pull/1988
* Various minor fixes to streaming
* 
## New Contributors
* @wjzijderveld made their first contribution in https://github.com/music-assistant/server/pull/1850
* @jdelaney72 made their first contribution in https://github.com/music-assistant/server/pull/2006
* @mcblum made their first contribution in https://github.com/music-assistant/server/pull/1988

**Full Changelog**: https://github.com/music-assistant/server/compare/2.5.0b8...2.5.0b9

# [2.5.0 BETA 8] - 06.03.2025

More fixes for streaming and announcements, especially on slower connections and better handling of super short audio clips.

More fixes for Tidal provider

# [2.5.0 BETA 7] - 05.03.2025

## What's Changed

* iBroadcast: Correct disc numbers in case the album has a disc number provided by @robsonke in https://github.com/music-assistant/server/pull/2000
* Adjust Tidal provider to a fully async implementation by @jozefKruszynski in https://github.com/music-assistant/server/pull/1995
* Fix stream errors and player getting into a loop of playing just a few seconds of each track
* Fix announcements

**Full Changelog**: https://github.com/music-assistant/server/compare/2.5.0b5...2.5.0b7

# [2.5.0 BETA 6] - 04.03.2025

## What's Changed

* Feat: Move the output limiter option from DSP to Player Settings by @maximmaxim345 in https://github.com/music-assistant/server/pull/1981
* Chore(deps): Bump pytest from 8.3.4 to 8.3.5 by @dependabot in https://github.com/music-assistant/server/pull/1999
* Chore(deps): Bump codespell from 2.3.0 to 2.4.1 by @dependabot in https://github.com/music-assistant/server/pull/1998
* ABS: fix for another unexpected API response by @fmunkes in https://github.com/music-assistant/server/pull/1994
* Add iTunes Podcast Search Provider by @fmunkes in https://github.com/music-assistant/server/pull/1977
* Chore(deps): Bump syrupy from 4.8.1 to 4.8.2 by @dependabot in https://github.com/music-assistant/server/pull/1996
* Audible provider: Fixes pagination and small cleanups by @ztripez in https://github.com/music-assistant/server/pull/1982
* frontend-2.12.1 by @music-assistant-machine in https://github.com/music-assistant/server/pull/2001
* Add more robust caching when internet speed is slow

**Full Changelog**: https://github.com/music-assistant/server/compare/2.5.0b5...2.5.0b6

# [2.5.0 BETA 5] - 01.03.2025

Fix audioerror (stream does not start) in some occasions

# [2.5.0 BETA 4] - 01.03.2025

Improvements to 
**Full Changelog**: https://github.com/music-assistant/server/compare/2.5.0b3...2.5.0b4

# [2.5.0 BETA 3] - 28.02.2025

## What’s Changed

### Server 2.5.0 BETA 3

## What's Changed

* Add caching of audio data to fix streams not starting fast enough by @marcelveldt in https://github.com/music-assistant/server/pull/1989
* Fix Large PodcastEpisode listings not working by @marcelveldt in https://github.com/music-assistant/server/pull/1991
* frontend-2.12.0 by @music-assistant-machine in https://github.com/music-assistant/server/pull/1993
* Various (very) small bugfixes and enhancements by @marcelveldt in https://github.com/music-assistant/server/pull/1992
* ABS: Login via API key by @fmunkes in https://github.com/music-assistant/server/pull/1990


**Full Changelog**: https://github.com/music-assistant/server/compare/2.4.2...2.5.0b3

### Frontend 2.12.0

## 🐛 Bugfixes

- #888 - Fix: Improved colors in fullscreen player (@maximmaxim345)
- #885 - Feat: improved Notification support (@maximmaxim345)
- #887 - Fix: Select all in search view (@maximmaxim345)

## 🚀 Features

- #885 - Feat: improved Notification support (@maximmaxim345)

## ⬆️ Dependencies

### Server

### Frontend

<details>
<summary>6 changes</summary>

- #879 - Chore(deps-dev): Bump prettier from 3.5.1 to 3.5.2 (@[dependabot[bot]](https://github.com/apps/dependabot))
- #880 - Chore(deps-dev): Bump @types/node from 22.13.4 to 22.13.5 (@[dependabot[bot]](https://github.com/apps/dependabot))
- #878 - Chore(deps-dev): Bump nanoid from 5.1.0 to 5.1.2 (@[dependabot[bot]](https://github.com/apps/dependabot))
- #889 - Chore(deps-dev): Bump vite from 6.1.0 to 6.2.0 (@[dependabot[bot]](https://github.com/apps/dependabot))
- #890 - Chore(deps): Bump vuetify from 3.7.12 to 3.7.14 (@[dependabot[bot]](https://github.com/apps/dependabot))
- #877 - Chore(deps-dev): Bump vue-tsc from 2.2.0 to 2.2.4 (@[dependabot[bot]](https://github.com/apps/dependabot))
</details>



# [2.5.0 Beta 2] - 27.02.2025

Fix crash at startup for some people

# [2.5.0 BETA 1] - 26.02.2025

## What’s Changed

### Server 2.5.0 BETA 1

## What's Changed

* Fix assertion error when trying to save a provider config by @marcelveldt in https://github.com/music-assistant/server/pull/1980
* fix(tidal): refresh access token correctly by @jozefKruszynski in https://github.com/music-assistant/server/pull/1984
* frontend-2.11.11 by @music-assistant-machine in https://github.com/music-assistant/server/pull/1987


**Full Changelog**: https://github.com/music-assistant/server/compare/2.5.0b0...2.5.0b1

### Frontend 2.11.11

Fix creation of player groups

**Full Changelog**: https://github.com/music-assistant/frontend/compare/2.11.10...2.11.11

## ⬆️ Dependencies

### Server

### Frontend



# [2.5.0 BETA 0] - 25.02.2025

**The start of the beta cycle for 2.5 !**

This version is on-par with the 2.4.0 stable version





















