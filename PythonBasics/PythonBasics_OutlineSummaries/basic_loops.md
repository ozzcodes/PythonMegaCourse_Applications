<h2> &nbsp; Summary: Loops</h2>
<div
    class='lecture-attachment lecture-attachment-type-text'
    id="lecture-attachment-23038303">
<p><p>In this section you learned that:</p><ul><li><strong>For loops</strong>are useful for executing a command over a large number of items.</li><li>You can create a&#xA0;<strong>for loop</strong>like so:</li></ul><pre class="ql-syntax" spellcheck="false">for letter in &apos;abc&apos;:
    print(letter.upper())
</pre><p>Output:</p><p><code>A</code></p><p><code>B</code></p><p><code>C</code></p><ul><li>The name after&#xA0;<code>for</code>(e.g.&#xA0;<code>letter</code>)&#xA0;is just a variable name</li><li><br></li><li>You can loop over&#xA0;<strong>dictionary keys</strong>:</li></ul><pre class="ql-syntax" spellcheck="false">phone_numbers = {&quot;John Smith&quot;:&quot;+37682929928&quot;,&quot;Marry Simpons&quot;:&quot;+423998200919&quot;}
for value in phone_numbers.keys():
    print(value)
</pre><p>Output:</p><p><code>John Smith</code></p><p><code>Marry Simpsons</code></p><ul><li>You can loop over&#xA0;<strong>dictionary values</strong>:</li></ul><pre class="ql-syntax" spellcheck="false">phone_numbers = {&quot;John Smith&quot;:&quot;+37682929928&quot;,&quot;Marry Simpons&quot;:&quot;+423998200919&quot;}
for value in phone_numbers.values():
    print(value)
</pre><p>Output:</p><p><code>+37682929928</code></p><p><code>+423998200919</code></p><ul><li>You can loop over&#xA0;<strong>dictionary items</strong>:</li></ul><pre class="ql-syntax" spellcheck="false">phone_numbers = {&quot;John Smith&quot;:&quot;+37682929928&quot;,&quot;Marry Simpons&quot;:&quot;+423998200919&quot;}
for key, value in phone_numbers.items():
    print(key, value)
</pre><ul><li>Output:&#xA0;</li><li><code>(&apos;John Smith&apos;, &apos;+37682929928&apos;)</code></li><li><code>(&apos;Marry Simpons&apos;, &apos;+423998200919&apos;)</code></li></ul><p><br></p><ul><li><strong>While loops</strong>will run as long as a condition is true:</li></ul><pre class="ql-syntax" spellcheck="false">while datetime.datetime.now() &lt; datetime.datetime(2090, 8, 20, 19, 30, 20):
    print(&quot;It&apos;s not yet 19:30:20 of 2090.8.20&quot;)
</pre><ul><li>The loop above will print out the string inside print() over and over again until the 20th of August, 2090.</li></ul><p><br></p>
</div>