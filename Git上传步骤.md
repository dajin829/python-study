# 上传 GitHub —— 每天收工三行

## 正常流程（每天一次）

VS Code 里按 `Ctrl + \`` 打开终端，确认光标前面是 `PS C:\Users\86185\Desktop\python-study>`，然后：

```
git add .
git commit -m "第 N 天：今天学的主题"
git push
```

- 一行一行粘，每行按一次回车，等光标重新出现再粘下一行。
- `git add .` 通常不显示任何东西，这是正常的。
- `commit` 后面引号里的字会显示在 GitHub 上，写清楚「第几天 + 学了什么」。别写 `save1`、`save2`，HR 第一眼看的就是这行字。
- 第一次才用 `git push -u origin main`，之后直接 `git push` 就行。

## 怎么看有没有成功

```
git status
```

第一行显示 `## main...origin/main` 就说明本地和 GitHub 同步了。
如果显示 `## main...origin/main [ahead 1]`，说明本地有 1 个提交没传上去，再跑一次 `git push`。

## 常见情况怎么办

| 看到什么 | 是什么意思 | 怎么办 |
|---|---|---|
| `nothing to commit, working tree clean` | 没有改动要提交 | 今天已经传过了，不用管，不是报错 |
| `[rejected] ... non-fast-forward` | GitHub 上的内容比本地新 | 先 `git pull --rebase origin main`，再 `git push` |
| 反复弹登录框 | 凭据失效 | 用户名 `dajin829`，密码栏填 classic token（`ghp_` 开头），不是 GitHub 登录密码 |
| 卡住不动超过 1 分钟 | 多半是网络 | Ctrl + C 中断，换手机热点再试 |

## 一句话记法

**add 收东西 → commit 打包贴标签 → push 发出去。**
