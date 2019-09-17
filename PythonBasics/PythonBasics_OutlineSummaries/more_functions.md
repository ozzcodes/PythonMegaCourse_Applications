 <h2>
    &nbsp;
    Summary: More on Functions
</h2>

  <!-- Attachment Blocks -->

  <div
    class='lecture-attachment lecture-attachment-type-text'
    id="lecture-attachment-23038960"
  >
    <div class="attachment-data"></div>
  </div>
 
<div class="lecture-text-container">
<p><p>In this section you learned that:</p><ul><li>Functions can have more than one&#xA0;<strong>parameter</strong>:</li></ul><pre class="ql-syntax" spellcheck="false">def volume(a, b, c):
    return a&#xA0;*&#xA0;b *&#xA0;c
</pre><ul><li>Functions can have&#xA0;<strong>default</strong>parameters (e.g.&#xA0;<code>coefficient</code>):</li></ul><pre class="ql-syntax" spellcheck="false">def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters

print(converter(10))
</pre><p>Output:&#xA0;<code>32.808</code></p><p>Arguments can be passed as&#xA0;<strong>non-keyword</strong>(positional) arguments (e.g.&#xA0;<code>a</code>) or&#xA0;<strong>keyword</strong>arguments (e.g.&#xA0;<code>b=2</code>and&#xA0;<code>c=10</code>):</p><pre class="ql-syntax" spellcheck="false">def volume(a, b, c):
    return a * b * c

print(volume(1, b=2, c=10))
</pre><ul><li>An&#xA0;<strong>*args&#xA0;</strong>parameter allows the&#xA0;function to be called with an arbitrary number of non-keyword arguments:</li></ul><pre class="ql-syntax" spellcheck="false">def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))
</pre><p>Output:&#xA0;<code>1001</code></p><ul><li>An&#xA0;<strong>**kwargs</strong>parameter allows the function to be called with an arbitrary number of keyword arguments:</li></ul><pre class="ql-syntax" spellcheck="false">def find_winner(**kwargs):
    return max(kwargs)
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
</pre><p>Output:&#xA0;<code>Sim</code></p><ul><li>Here&apos;s a summary of function elements:</li></ul><p></p>
</div>
