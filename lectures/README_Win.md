### Windows 注意事项

在Windows系统上运行本工具时，建议注意以下事项：

1. **使用 UTF-8 编码**：含中文或 emoji 的源文件可能触发 `UnicodeEncodeError` / `UnicodeDecodeError`。有两种解决方式：
   - 方式 A（改代码，推荐）：在 `execute.py` 开头添加：
     ```python
     import sys
     sys.stdout.reconfigure(encoding='utf-8')
     sys.stderr.reconfigure(encoding='utf-8')
     ```
     并在读取文件时指定编码：`open(path, encoding="utf-8")`。
   - 方式 B（改命令）：执行时临时设置环境变量：
     ```powershell
     $env:PYTHONIOENCODING='utf-8'
     python execute.py -m lecture_01
     ```

2. **创建前端静态文件符号链接**（仅首次）：
   Vite 仅提供 `public/` 目录下的静态文件，因此需在 `trace-viewer/public/` 下创建指向上级目录的链接，以便正确加载 trace JSON 与图片：
   ```cmd
   cd trace-viewer
   mklink /J public\images ..\images
   mklink /J public\var ..\var
   ```

3. **稳定开启 Vite 开发服务器**：
   直接运行 `npm run dev` 会在前台阻塞，终端超时后进程自动终止。建议用 `Start-Process` 在后台启动：
   ```powershell
   cd trace-viewer
   $vite = "$(Get-Location)\node_modules\.bin\vite.cmd"
   Start-Process -NoNewWindow -FilePath $vite
   ```
   如需停止：`Get-Process -Name "node" | Stop-Process`
