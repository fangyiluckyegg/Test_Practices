/*题目描述
输入两个整数 a,b，输出它们的和。
输入格式:输入两个以空格分隔的整数 a,b。
输出格式:输出一个整数，表示 a+b。
*/

import java.util.Scanner;

public class Yyrm_P1001 {
//文件名编写标准：Java类名必须和文件名一致-Yyrm_P1001.java）
    public static void main(String args[]) {
    //主函数编写标准：public static void main(String args[])
        Scanner cin = new Scanner(System.in);
        //输入输出类标准写法：Scanner cin = new Scanner(System.in);
        int a = cin.nextInt(), b = cin.nextInt();
        //作用：读取一个整数，自动跳过空格、回车、Tab，返回 int 值
        System.out.println(a + b);
        //作用：计算a+b的结果，然后打印到控制台，打印完自动换行
        cin.close();
        //作用：关闭 Scanner，释放输入资源
    }
}

/*Python版本
a, b = map(int, input().split())
print(a + b)
*/
/* 
作用：读取一行输入，按空格分割，转成两个整数，分别赋值给a和b
- `input()`：读取一行键盘输入（读到回车为止）
- `.split()`：把这一行字符串，按空格切开，得到字符串列表
- `map(int, ...)`：把列表里每一个字符串转成整数
- `a, b = ...`：解包，依次放进变量 a、b
*/

/*C++版本
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}
*/

/*
#C++是编译型语言，不是解释型Python/Java不一样：
- Python：解释器直接读 `.py` 源码，逐行解释执行，**不需要先打包成独立 exe**
- Java：`javac` 先编译成 `.class`（字节码），再由 JVM 跑 class，不是直接给操作系统跑
- C++：**源码不能直接给 CPU 执行**，必须经过：
`cpp源码 → 编译（翻译成汇编→机器码）→ 链接 → 可执行文件`
*/

