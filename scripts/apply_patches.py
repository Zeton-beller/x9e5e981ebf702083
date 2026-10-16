import os, sys

target_file = os.path.join(os.path.dirname(__file__), '..', 'libultraship', 'src', 'ship', 'port', 'switch', 'SwitchImpl.cpp')
if not os.path.exists(target_file):
    print(f"Warning: {target_file} not found!")
    sys.exit(0)

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

if 'PlSharedFontType_ChineseSimplified' in content:
    print("SwitchImpl.cpp already patched for Chinese font support.")
    sys.exit(0)

target = '''    PlFontData fonts_std;
    PlFontData fonts_ext;

    plGetSharedFontByType(&fonts_std, PlSharedFontType_Standard);
    plGetSharedFontByType(&fonts_ext, PlSharedFontType_NintendoExt);

    ImFontConfig config;
    config.FontDataOwnedByAtlas = false;

    strcpy(config.Name, "Nintendo Standard");
    fonts->AddFontFromMemoryTTF(fonts_std.address, fonts_std.size, 24.0f, &config, fonts->GetGlyphRangesCyrillic());

    strcpy(config.Name, "Nintendo Ext");'''

replacement = '''    PlFontData fonts_std;
    PlFontData fonts_ext;
    PlFontData fonts_cn;

    plGetSharedFontByType(&fonts_std, PlSharedFontType_Standard);
    plGetSharedFontByType(&fonts_ext, PlSharedFontType_NintendoExt);
    bool has_cn = R_SUCCEEDED(plGetSharedFontByType(&fonts_cn, PlSharedFontType_ChineseSimplified));

    ImFontConfig config;
    config.FontDataOwnedByAtlas = false;

    strcpy(config.Name, "Nintendo Standard");
    fonts->AddFontFromMemoryTTF(fonts_std.address, fonts_std.size, 24.0f, &config, fonts->GetGlyphRangesCyrillic());

    if (has_cn) {
        ImFontConfig cn_config;
        cn_config.FontDataOwnedByAtlas = false;
        cn_config.MergeMode = true;
        strcpy(cn_config.Name, "Nintendo ChineseSimplified");
        fonts->AddFontFromMemoryTTF(fonts_cn.address, fonts_cn.size, 24.0f, &cn_config, fonts->GetGlyphRangesChineseFull());
    }

    strcpy(config.Name, "Nintendo Ext");
    config.MergeMode = true;'''

if target in content:
    content = content.replace(target, replacement, 1)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully patched SwitchImpl.cpp for Chinese font support!")
else:
    print("Error: Target anchor not found in SwitchImpl.cpp!")
    sys.exit(1)
