/*题目描述:
给定一个3位整数n，计算：
1.n的各位数字之和；
2.n的各位数字之和的平方；
3.n的各位数字之和的立方；
例如，当这个三位数是 123 时：
各位数字之和为：1+2+3=6；
各位数字之和的平方为：(1+2+3) 2 =(1+2+3)×(1+2+3)=36；
各位数字之和的立方为：(1+2+3) 3 =(1+2+3)×(1+2+3)×(1+2+3)=216。
输入格式
输入只有一行一个三位整数 n。
输出格式
输出共三行，第一行为各位数字之和，第二行为各位数字之和的平方，第三行为各位数字之和的立方。
*/

import java.util.Scanner;

public class Yyrm_B3685 {
    //文件名编写标准：Java类名必须和文件名一致-Yyrm_B3685.java）
    public static void main(String args[]) {
        Scanner cin = new Scanner(System.in);
        //输入输出类标准写法：Scanner num = new Scanner(System.in);
        int num = cin.nextInt();
        //作用：读取一个整数，自动跳过空格、回车、Tab，返回 int 值
        int a = num / 100; 
        //作用：整数除法，取出三位数的百位数字（只保留整数部分，直接砍掉小数，不四舍五入）
        int b = (num / 10) % 10; 
        //作用：先整数除法，取出三位数的前两位数字，然后再对 10 取余，得到十位数字
        int c = num % 10; 
        //作用：对 10 取余，得到个位数字
        int sum = a + b + c;
        System.out.println(sum);
        System.out.println(sum * sum);
        System.out.println(sum * sum * sum);

        cin.close();
        //作用：关闭 Scanner，释放输入资源
    }   
}

/*Python版本
num = input()
a = int(num[0]) #取百位
b = int(num[1]) #取十位   
c = int(num[2]) #取个位
sum = a + b + c
print(sum)
print(sum ** 2)
print(sum ** 3) 
*/
/* 
#作用：取出字符串num的第0号位字符，再转成整数,即取百位
> 前提：`num`是字符串类型（一般是`num = input()`读进来的）
> 下标从 0开始：`num[0]`是第一个字符
*/

/*C++版本
#include <iostream>
using namespace std;

int main() {
    int num;
    cin >> num;
    int a = num / 100; //取百位
    //作用：整数除法，取出三位数的百位数字（只保留整数部分，直接砍掉小数，不四舍五入）
    int b = (num / 10) % 10; //取十位
    //作用：先整数除法，取出三位数的前两位数字，然后再对 10 取余，得到十位数字
    int c = num % 10; //取个位
    //作用：对 10 取余，得到个位数字
    int sum = a + b + c;
    cout << sum << endl;
    cout << sum * sum << endl; 
    cout << sum * sum * sum << endl;
    return 0;
    //作用:放在 `int main()` 的最后一行：告诉操作系统：程序正常结束，没有出错
}
*/

/*
#C++是编译型语言，不是解释型Python/Java不一样：
- Python：解释器直接读 `.py` 源码，逐行解释执行，**不需要先打包成独立 exe**
- Java：`javac` 先编译成 `.class`（字节码），再由 JVM 跑 class，不是直接给操作系统跑
- C++：**源码不能直接给 CPU 执行**，必须经过：
`cpp源码 → 编译（翻译成汇编→机器码）→ 链接 → 可执行文件`
*/