# Time Complexity : O(1)

---
**Question** : In Ciel's restaurant, a waiter is training. Since the waiter isn't good at arithmetic, sometimes he gives guests wrong change. Ciel gives him a simple problem. What is A-B (A minus B) ?

Surprisingly, his answer is wrong. To be more precise, his answer has exactly one wrong digit. Can you imagine this? Can you make the same mistake in this problem?

---
**LOGIC** : <br /><br/>
*CASE 1* : If the number is positive, simply add one to it ... but wait what if the number is 29 or something that ends in 9, 
the logic does not work :( thus I substracted 2 from the number if the number becomes something divisible by 10, thus all digits will remain same but one !!
<br/><br/>
*CASE 2* : Think this in reverse !!

---
