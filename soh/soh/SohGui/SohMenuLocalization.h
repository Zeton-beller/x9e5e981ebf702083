#ifndef SOH_MENU_LOCALIZATION_H
#define SOH_MENU_LOCALIZATION_H

#include <string>
#include <unordered_map>
#include "soh/SohGui/MenuTypes.h"
#include <imgui.h>

namespace SohGui {
    bool IsMenuLocalizationEnabled();
    const ImWchar* GetChineseFontGlyphRanges(ImFontAtlas* fonts);
    void ApplySohMenuLocalization(std::unordered_map<std::string, MainMenuEntry>& menuEntries);
    std::string TranslateSidebar(const std::string& sidebar);
    std::string TranslateHeader(const std::string& header);
    std::string TranslateWidgetName(const std::string& name);
    std::string TranslateTooltip(const std::string& tooltip);
    std::string TranslateOption(const std::string& option);
    const char* TranslateComboOption(const char* option);
}

#endif // SOH_MENU_LOCALIZATION_H
