# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src\\mammography_visualization.py'],
             pathex=['D:\\Victor\\uaslp\\Semestre 7\\vision computacional\\Proyecto\\Repositorio\\Support-system-for-reading-mammograms'],
             binaries=[],
             datas=[('src/example.dcm', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
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
          name='mammography_visualization',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mammography_visualization')
