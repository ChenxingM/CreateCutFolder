# 卡文件夹管理系统

这是一个用于创建和管理卡文件夹的 Python 脚本。用户可以批量创建文件夹、列出现有文件夹，以及删除指定的文件夹。

## 功能

1. 创建单个或多个卡文件夹。
2. 列出当前所有卡文件夹。
3. 删除指定的卡文件夹。

## 文件结构

生成的文件夹结构如下：
```
epnd_cxxx_lo/
    ├── _bg/
    ├── _clip/
    ├── _conte/
    ├── _info/
    ├── _lo/
    ├── _pool/
    └── _sheet/
    └── epnd_cxxx_v01_1920816_hon.aep
```

## 使用方法

### 依赖

此脚本依赖于以下 Python 标准库：
- os
- shutil
- re

确保你已安装 Python 并具有以上库。

### 运行脚本

1. 克隆本仓库到你的本地机器：

```bash
git clone https://github.com/ChenxingM/CreateCutFolder.git
```

2. 导航到项目目录：

```bash
cd CreateCutFolder
```

3. 修改脚本中的基础路径和源文件路径：

```python
base_path = r"/path/to/your/base/directory"
aep_file = r"/path/to/your/source/file/epnd_c000_v01_1920816_hon.aep"
```

4. 运行脚本：

```bash
python create_cut_folders.py
```

### 脚本交互

运行脚本后，你可以通过输入以下命令进行交互：

- 输入 `ls` 列出当前所有卡文件夹。
- 输入 `rm` 删除指定的卡文件夹（会先列出所有卡文件夹，要求确认删除）。
- 输入单个数字（如 `5`）创建对应编号的卡文件夹。
- 输入范围（如 `1-100`）批量创建文件夹。

### 示例

以下是一个示例交互：

```plaintext
创建卡文件夹系统
输入卡号: ls
当前卡有:
014
000
024
001
999

输入卡号: 1-10
创建卡文件夹: epnd_c001_lo
复制AEP到: /path/to/your/base/directory/epnd_c001_lo/epnd_c001_v01_1920816_hon.aep
...
创建卡文件夹: epnd_c010_lo
复制AEP到: /path/to/your/base/directory/epnd_c010_lo/epnd_c010_v01_1920816_hon.aep

输入卡号: rm
当前卡有:
014
000
024
001
999
001
002
003
...
010
输入要删除的卡号: 5
确认删除卡文件夹 epnd_c005_lo 吗？(y/n): y
已删除卡文件夹: epnd_c005_lo
```

## 贡献

欢迎提交问题与请求。如果你想贡献，请 fork 本仓库并提交 PR。

## 许可证

此项目使用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。