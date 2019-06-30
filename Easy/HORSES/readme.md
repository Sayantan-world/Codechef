# Time Complexity : O(nlog(n))
[Excluding the loop for test cases]
### Language : PYPY3
---
**Question** : Chef is very fond of horses. He enjoys watching them race. As expected, he has a stable full of horses. He, along with his friends, goes to his stable during the weekends to watch a few of these horses race. Chef wants his friends to enjoy the race and so he wants the race to be close. This can happen only if the horses are comparable on their skill i.e. the difference in their skills is less.

There are N horses in the stable. The skill of the horse i is represented by an integer S[i]. The Chef needs to pick 2 horses for the race such that the difference in their skills is minimum. This way, he would be able to host a very interesting race. Your task is to help him do this and report the minimum difference that is possible between 2 horses in the race.

---
**LOGIC** : <br /><br/>
There can be various ways to solve this problem.<br/>
Naive way: Run a nested loop and keep checking each and every element to find minimum difference<br/>
Better way : First we sort the list O(nlog(n)) and then run a loop to find the minimum difference

---
