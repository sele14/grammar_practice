# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\Administrator\\Dropbox\\Files\\Skole\\UiB Matematikk 17-18\\Vår 18\\INF109\\Oppgaver\\Language practice'],
             pathex=['C:\\Users\\Administrator\\Dropbox\\Files\\Skole\\UiB Matematikk 17-18\\Vår 18\\INF109\\Oppgaver\\Language practice'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Language practice',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
