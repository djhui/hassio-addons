#!/bin/sh



mkdir -p /config/addons_config/wechat-server 

if [ ! -f "/config/addons_config/wechat-server/Wechat_Robot.py" ]; then
cp /Wechat_Robot.py /config/addons_config/wechat-server/Wechat_Robot.py
fi
if [ ! -f "/config/addons_config/wechat-server/config.ini" ]; then
cp /config.ini /config/addons_config/wechat-server/config.ini
fi



python /config/addons_config/wechat-server/Wechat_Robot.py
