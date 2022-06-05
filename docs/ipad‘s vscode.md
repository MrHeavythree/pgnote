# How to build an environment similar to vscode on iPad?

> Keywords: iPad vscode

## Introduction

The iPad tablet launched by apple, as a product between PC and mobile phone, has great advantages over PC in portability.Since iPad is obviously better than PC in portability, why not use iPad for program development?

Visual Studio Code (hereinafter referred to as vscode), as a lightweight text editor launched by Microsoft, is famous for its lightweight and multi plug-ins. It is the choice of many programmers.

Although vscode is a fairly good editor in programming, it cannot be installed for iPad.

Since the iPad can't use native vscode, why don't we build a similar one?

## Works

First, let's clarify our thinking.

![our thinking](assets/example-1-1.jpg)

We first install code server through ECs, and then we can use it to use vscode on iPad.

Let's do it in turn.

1.First, we need a cloud server.I am using the Ubuntu system of Tencent cloud.
![Tencent cloud](assets/example-1-2.jpg)
2.After logging in to ECs, we should use the following script to install according to the official document of code server:

```
    curl -fsSL https://code-server.dev/install.sh | sh
```

3.After installing code server, we can start code server with the following command:

```
    code-server --host "0.0.0.0"
```

Pay attention, that the following parameters are **required**, otherwise the machine outside the server cannot be connected.In addition to setting this parameter, you also need to set the allowed port 8080 access on the security group of the server.

After configuration, you can use "public IP: 8080" on the browser to access the web version of vscode.
The first time you open it, you will ask for the password. The password is in ~/. config/code-server/config.yaml file.

![Picture](assets/example-1-3.jpg)

4.Let vscode run in the background all the time
When the login window of Tencent cloud is closed, vscode will stop. At this time, it needs to run in the background all the time. The steps are as follows:
(1) Install screen

`
apt-get install screen
`

(2) Create a new window after installation,

`
screen -S codeserver
`

(3) After entering the window, run code server, and then Ctrl + A + D to switch the Linux window. You will find that it will not be interrupted.

Here, the work of building an environment similar to vscode on iPad is officially over.

## Thanks

Thank you very much for answering Lord Zhihu @熊的一些事, your column [here](https://zhuanlan.zhihu.com/p/436011162) is the main content of this article about building an environment. Thank Zhihu for pushing this column to me.
