# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started.

import octoprint.plugin

class RepraspPlugin(octoprint.plugin.StartupPlugin,
                    octoprint.plugin.TemplatePlugin,
                    octoprint.plugin.SettingsPlugin
                    octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
            self._logger.info("RepRasp UI Loaded! (more: %s)" % self._settings.get(["url"]))
            
    def get_settings_defaults(self):
            return dict(url="https://en.wikipedia.org/wiki/Hello_world")
            
    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
         return dict(
             js=["js/reprasp.js"]
             css=["css/reprasp.css"],
             less=["less/reprasp.less"]
         )
         
__plugin_name__ = "RepRasp UI"
__plugin_implementation__ = RepraspPlugin()