# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from chromewhip.chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.chromewhip.protocol import dom as DOM
from chromewhip.chromewhip.protocol import page as Page
from chromewhip.chromewhip.protocol import runtime as Runtime

# ScreenOrientation: Screen orientation.
class ScreenOrientation(ChromeTypeBase):
    def __init__(self,
                 type: Union['str'],
                 angle: Union['int'],
                 ):

        self.type = type
        self.angle = angle


# VirtualTimePolicy: advance: If the scheduler runs out of immediate work, the virtual time base may fast forward toallow the next delayed task (if any) to run; pause: The virtual time base may not advance;pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pendingresource fetches.
VirtualTimePolicy = str

class Emulation(PayloadMixin):
    """ This domain emulates different environments for the page.
    """
    @classmethod
    def canEmulate(cls):
        """Tells whether emulation is supported.
        """
        return (
            cls.build_send_payload("canEmulate", {
            }),
            cls.convert_payload({
                "result": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def clearDeviceMetricsOverride(cls):
        """Clears the overriden device metrics.
        """
        return (
            cls.build_send_payload("clearDeviceMetricsOverride", {
            }),
            None
        )

    @classmethod
    def clearGeolocationOverride(cls):
        """Clears the overriden Geolocation Position and Error.
        """
        return (
            cls.build_send_payload("clearGeolocationOverride", {
            }),
            None
        )

    @classmethod
    def resetPageScaleFactor(cls):
        """Requests that page scale factor is reset to initial values.
        """
        return (
            cls.build_send_payload("resetPageScaleFactor", {
            }),
            None
        )

    @classmethod
    def setFocusEmulationEnabled(cls,
                                 enabled: Union['bool'],
                                 ):
        """Enables or disables simulating a focused and active page.
        :param enabled: Whether to enable to disable focus emulation.
        :type enabled: bool
        """
        return (
            cls.build_send_payload("setFocusEmulationEnabled", {
                "enabled": enabled,
            }),
            None
        )

    @classmethod
    def setCPUThrottlingRate(cls,
                             rate: Union['float'],
                             ):
        """Enables CPU throttling to emulate slow CPUs.
        :param rate: Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
        :type rate: float
        """
        return (
            cls.build_send_payload("setCPUThrottlingRate", {
                "rate": rate,
            }),
            None
        )

    @classmethod
    def setDefaultBackgroundColorOverride(cls,
                                          color: Optional['DOM.RGBA'] = None,
                                          ):
        """Sets or clears an override of the default background color of the frame. This override is used
if the content does not specify one.
        :param color: RGBA of the default background color. If not specified, any existing override will be
cleared.
        :type color: DOM.RGBA
        """
        return (
            cls.build_send_payload("setDefaultBackgroundColorOverride", {
                "color": color,
            }),
            None
        )

    @classmethod
    def setDeviceMetricsOverride(cls,
                                 width: Union['int'],
                                 height: Union['int'],
                                 deviceScaleFactor: Union['float'],
                                 mobile: Union['bool'],
                                 scale: Optional['float'] = None,
                                 screenWidth: Optional['int'] = None,
                                 screenHeight: Optional['int'] = None,
                                 positionX: Optional['int'] = None,
                                 positionY: Optional['int'] = None,
                                 dontSetVisibleSize: Optional['bool'] = None,
                                 screenOrientation: Optional['ScreenOrientation'] = None,
                                 viewport: Optional['Page.Viewport'] = None,
                                 ):
        """Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
query results).
        :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :type width: int
        :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :type height: int
        :param deviceScaleFactor: Overriding device scale factor value. 0 disables the override.
        :type deviceScaleFactor: float
        :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text
autosizing and more.
        :type mobile: bool
        :param scale: Scale to apply to resulting view image.
        :type scale: float
        :param screenWidth: Overriding screen width value in pixels (minimum 0, maximum 10000000).
        :type screenWidth: int
        :param screenHeight: Overriding screen height value in pixels (minimum 0, maximum 10000000).
        :type screenHeight: int
        :param positionX: Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
        :type positionX: int
        :param positionY: Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
        :type positionY: int
        :param dontSetVisibleSize: Do not set visible view size, rely upon explicit setVisibleSize call.
        :type dontSetVisibleSize: bool
        :param screenOrientation: Screen orientation override.
        :type screenOrientation: ScreenOrientation
        :param viewport: If set, the visible area of the page will be overridden to this viewport. This viewport
change is not observed by the page, e.g. viewport-relative elements do not change positions.
        :type viewport: Page.Viewport
        """
        return (
            cls.build_send_payload("setDeviceMetricsOverride", {
                "width": width,
                "height": height,
                "deviceScaleFactor": deviceScaleFactor,
                "mobile": mobile,
                "scale": scale,
                "screenWidth": screenWidth,
                "screenHeight": screenHeight,
                "positionX": positionX,
                "positionY": positionY,
                "dontSetVisibleSize": dontSetVisibleSize,
                "screenOrientation": screenOrientation,
                "viewport": viewport,
            }),
            None
        )

    @classmethod
    def setScrollbarsHidden(cls,
                            hidden: Union['bool'],
                            ):
        """
        :param hidden: Whether scrollbars should be always hidden.
        :type hidden: bool
        """
        return (
            cls.build_send_payload("setScrollbarsHidden", {
                "hidden": hidden,
            }),
            None
        )

    @classmethod
    def setDocumentCookieDisabled(cls,
                                  disabled: Union['bool'],
                                  ):
        """
        :param disabled: Whether document.coookie API should be disabled.
        :type disabled: bool
        """
        return (
            cls.build_send_payload("setDocumentCookieDisabled", {
                "disabled": disabled,
            }),
            None
        )

    @classmethod
    def setEmitTouchEventsForMouse(cls,
                                   enabled: Union['bool'],
                                   configuration: Optional['str'] = None,
                                   ):
        """
        :param enabled: Whether touch emulation based on mouse input should be enabled.
        :type enabled: bool
        :param configuration: Touch/gesture events configuration. Default: current platform.
        :type configuration: str
        """
        return (
            cls.build_send_payload("setEmitTouchEventsForMouse", {
                "enabled": enabled,
                "configuration": configuration,
            }),
            None
        )

    @classmethod
    def setEmulatedMedia(cls,
                         media: Union['str'],
                         ):
        """Emulates the given media for CSS media queries.
        :param media: Media type to emulate. Empty string disables the override.
        :type media: str
        """
        return (
            cls.build_send_payload("setEmulatedMedia", {
                "media": media,
            }),
            None
        )

    @classmethod
    def setGeolocationOverride(cls,
                               latitude: Optional['float'] = None,
                               longitude: Optional['float'] = None,
                               accuracy: Optional['float'] = None,
                               ):
        """Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
unavailable.
        :param latitude: Mock latitude
        :type latitude: float
        :param longitude: Mock longitude
        :type longitude: float
        :param accuracy: Mock accuracy
        :type accuracy: float
        """
        return (
            cls.build_send_payload("setGeolocationOverride", {
                "latitude": latitude,
                "longitude": longitude,
                "accuracy": accuracy,
            }),
            None
        )

    @classmethod
    def setNavigatorOverrides(cls,
                              platform: Union['str'],
                              ):
        """Overrides value returned by the javascript navigator object.
        :param platform: The platform navigator.platform should return.
        :type platform: str
        """
        return (
            cls.build_send_payload("setNavigatorOverrides", {
                "platform": platform,
            }),
            None
        )

    @classmethod
    def setPageScaleFactor(cls,
                           pageScaleFactor: Union['float'],
                           ):
        """Sets a specified page scale factor.
        :param pageScaleFactor: Page scale factor.
        :type pageScaleFactor: float
        """
        return (
            cls.build_send_payload("setPageScaleFactor", {
                "pageScaleFactor": pageScaleFactor,
            }),
            None
        )

    @classmethod
    def setScriptExecutionDisabled(cls,
                                   value: Union['bool'],
                                   ):
        """Switches script execution in the page.
        :param value: Whether script execution should be disabled in the page.
        :type value: bool
        """
        return (
            cls.build_send_payload("setScriptExecutionDisabled", {
                "value": value,
            }),
            None
        )

    @classmethod
    def setTouchEmulationEnabled(cls,
                                 enabled: Union['bool'],
                                 maxTouchPoints: Optional['int'] = None,
                                 ):
        """Enables touch on platforms which do not support them.
        :param enabled: Whether the touch event emulation should be enabled.
        :type enabled: bool
        :param maxTouchPoints: Maximum touch points supported. Defaults to one.
        :type maxTouchPoints: int
        """
        return (
            cls.build_send_payload("setTouchEmulationEnabled", {
                "enabled": enabled,
                "maxTouchPoints": maxTouchPoints,
            }),
            None
        )

    @classmethod
    def setVirtualTimePolicy(cls,
                             policy: Union['VirtualTimePolicy'],
                             budget: Optional['float'] = None,
                             maxVirtualTimeTaskStarvationCount: Optional['int'] = None,
                             waitForNavigation: Optional['bool'] = None,
                             initialVirtualTime: Optional['Network.TimeSinceEpoch'] = None,
                             ):
        """Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
the current virtual time policy.  Note this supersedes any previous time budget.
        :param policy: 
        :type policy: VirtualTimePolicy
        :param budget: If set, after this many virtual milliseconds have elapsed virtual time will be paused and a
virtualTimeBudgetExpired event is sent.
        :type budget: float
        :param maxVirtualTimeTaskStarvationCount: If set this specifies the maximum number of tasks that can be run before virtual is forced
forwards to prevent deadlock.
        :type maxVirtualTimeTaskStarvationCount: int
        :param waitForNavigation: If set the virtual time policy change should be deferred until any frame starts navigating.
Note any previous deferred policy change is superseded.
        :type waitForNavigation: bool
        :param initialVirtualTime: If set, base::Time::Now will be overriden to initially return this value.
        :type initialVirtualTime: Network.TimeSinceEpoch
        """
        return (
            cls.build_send_payload("setVirtualTimePolicy", {
                "policy": policy,
                "budget": budget,
                "maxVirtualTimeTaskStarvationCount": maxVirtualTimeTaskStarvationCount,
                "waitForNavigation": waitForNavigation,
                "initialVirtualTime": initialVirtualTime,
            }),
            cls.convert_payload({
                "virtualTimeTicksBase": {
                    "class": float,
                    "optional": False
                },
            })
        )

    @classmethod
    def setTimezoneOverride(cls,
                            timezoneId: Union['str'],
                            ):
        """Overrides default host system timezone with the specified one.
        :param timezoneId: The timezone identifier. If empty, disables the override and
restores default host system timezone.
        :type timezoneId: str
        """
        return (
            cls.build_send_payload("setTimezoneOverride", {
                "timezoneId": timezoneId,
            }),
            None
        )

    @classmethod
    def setVisibleSize(cls,
                       width: Union['int'],
                       height: Union['int'],
                       ):
        """Resizes the frame/viewport of the page. Note that this does not affect the frame's container
(e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
on Android.
        :param width: Frame width (DIP).
        :type width: int
        :param height: Frame height (DIP).
        :type height: int
        """
        return (
            cls.build_send_payload("setVisibleSize", {
                "width": width,
                "height": height,
            }),
            None
        )

    @classmethod
    def setUserAgentOverride(cls,
                             userAgent: Union['str'],
                             acceptLanguage: Optional['str'] = None,
                             platform: Optional['str'] = None,
                             ):
        """Allows overriding user agent with the given string.
        :param userAgent: User agent to use.
        :type userAgent: str
        :param acceptLanguage: Browser langugage to emulate.
        :type acceptLanguage: str
        :param platform: The platform navigator.platform should return.
        :type platform: str
        """
        return (
            cls.build_send_payload("setUserAgentOverride", {
                "userAgent": userAgent,
                "acceptLanguage": acceptLanguage,
                "platform": platform,
            }),
            None
        )



class VirtualTimeBudgetExpiredEvent(BaseEvent):

    js_name = 'Emulation.virtualTimeBudgetExpired'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
