// Problem 1: Contest Timing [Brian Dean] 
// 问题一：比赛时间安排 [Brian Dean]

/*Bessie the cow is getting bored of the milk production industry, and wants 
to switch to an exciting new career in computing.  To improve her coding
skills, she decides to compete in the on-line USACO competitions.  Since
she notes that the contest starts on November 11, 2011 (11/11/11), she
decides for fun to download the problems and begin coding at exactly 11:11
AM on 11/11/11.*/

/*奶牛贝西对牛奶生产行业感到厌倦，想要
转向一个令人兴奋的新职业——计算机领域。为了提升她的编码能力
技能提升后，她决定参加线上USACO比赛。因为
她指出比赛将于2011年11月11日（11/11/11）开始，她
为了好玩，决定在11：11正好下载题目并开始编码
上午，2011年11月11日。*/

/*Unfortunately, Bessie's time management ability is quite poor, so she wants
to write a quick program to help her make sure she does not take longer
than the 3 hour (180 minute) time limit for the contest.  Given the date
and time she stops working, please help Bessie compute the total number of
minutes she will have spent on the contest.*/

/*不幸的是，贝茜的时间管理能力很差，所以她想要
写一个快速程序，帮助她确保不会耽搁更久
超过比赛的3小时（180分钟）时间限制。根据日期
她停止工作时，请帮贝西计算总数
她在比赛中花费的时间。*/


// PROBLEM NAME: ctiming  
// 问题名称：ctiming
/*INPUT FORMAT:
* Line 1: This line contains 3 space-separated integers, D H M,
        specifying the date and time at which Bessie ends the contest.
        D will be an integer in the range 11..14 telling the day of
        the month; H and M are hours and minutes on a 24-hour clock
        (so they range from H=0,M=0 at midnight up through H=23,M=59
        at 11:59 PM).
SAMPLE INPUT (file ctiming.in):
12 13 14*/

/*输入格式：
* 第 1 行：此行包含 3 个空格分隔的整数，D H M，
 并指定贝西结束比赛的日期和时间。
 D 将是 11.14 范围内的一个整数，表示当天
 月份;H和M是24小时制中的小时和分钟
 （因此它们的范围从午夜的H=0，M=0一直到H=23，M=59）
 晚上11：59）。
示例输入（文件 ctiming.in）：
12 13 14*/

/*INPUT DETAILS:
Bessie ends the contest on November 12, at 13:14 (that is, at 1:14 PM).
OUTPUT FORMAT:
* Line 1: The total number of minutes spent by Bessie in the contest,
        or -1 if her ending time is earlier than her starting time.
SAMPLE OUTPUT (file ctiming.out):
1563
OUTPUT DETAILS:
Bessie ends the contest 1563 minutes after she starts.*/

/*输入详情：
贝西将在11月12日13：14（也就是下午1：14）结束比赛。
输出格式：
* 第1行：贝西在比赛中的总出场时间，
 或者如果她的结束时间早于起始时间，则为-1。
示例输出（文件 ctiming.out）：
1563
输出详情：
贝西在开始比赛后1563分钟结束比赛。*/

/*Solution Notes: A key to making the problem easy to solve is to write a function that converts from (day, hour, minute) to a single integer that reflects an absolute count of number of minutes since some pre-determined starting point. In the sample C solution below, the function total_mins() computes the total number of minutes elapsed since the beginning of the month. Using this function, it is now easy to compute the number of minutes in the difference of two dates - we first convert the two dates into integers, and then simply subtract!*/

/*解决方案说明：让问题容易解决的关键是写一个函数，将（日、时、分钟）转换为一个整数，反映自某个预设起点以来的绝对分钟数。在下面的示例 C 解中，函数 total_mins（） 计算自月初以来的总分钟数。利用这个函数，现在很容易计算两个日期差的分钟数——我们先把两个日期换算成整数，然后简单减去！*/

/*
ID: fangyil1
TASK: test
LANG: C++                 
*/

#include <stdio.h>

int total_mins(int d, int h, int m)
{
  return d * 24 * 60 + h * 60 + m;
}

int main(void)
{
  int d, h, m;
  
  freopen ("ctiming.in", "r", stdin);
  freopen ("ctiming.out", "w", stdout);

  scanf ("%d %d %d", &d, &h, &m);
  
  if (total_mins(d,h,m) < total_mins(11,11,11))
    printf ("-1\n");
  else
    printf ("%d\n", total_mins(d,h,m) - total_mins(11,11,11));

  return 0;
}