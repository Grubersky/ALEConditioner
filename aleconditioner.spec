# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             #datas=[("assets\\", "assets\\"), ("libs\\kv\\", "libs\\kv\\")],
             datas=[
             ("main.py", '.'),
             ("main_ui.kv", '.'),
             ("entitlements.plist", '.'),
             ("Backdrop.png", '.'),
             ("ale_icon.icns", '.'),
             ("ale_icon.png", '.')
             ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=['_tkinter', 'Tkinter', 'enchant', 'twisted'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='aleconditioner',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          #codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='aleconditioner')
app = BUNDLE(coll,
             name='ALE Conditioner.app',
             icon='ale_icon.icns',
             bundle_identifier='com.potatocode.marcogruber.aleconditioner')

