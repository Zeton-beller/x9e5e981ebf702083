#ifdef __SWITCH__
#include "SwitchFontHelper.h"
#include <switch.h>

bool Switch_GetChineseSharedFont(void** outAddress, size_t* outSize) {
    static bool sPlInited = false;
    static PlFontData sPlFontCn;
    static bool sHasPlFontCn = false;
    if (!sPlInited) {
        Result rc = plInitialize(PlServiceType_User);
        if (R_SUCCEEDED(rc)) {
            sHasPlFontCn = R_SUCCEEDED(plGetSharedFontByType(&sPlFontCn, PlSharedFontType_ChineseSimplified));
        }
        sPlInited = true;
    }

    if (sHasPlFontCn && sPlFontCn.address != nullptr && sPlFontCn.size > 0) {
        if (outAddress) {
            *outAddress = sPlFontCn.address;
        }
        if (outSize) {
            *outSize = sPlFontCn.size;
        }
        return true;
    }
    return false;
}
#endif
