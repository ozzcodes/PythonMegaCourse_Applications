<h2>
    &nbsp;
    Summary: List Comprehensions
</h2>

  <!-- Attachment Blocks -->

  <div
    class='lecture-attachment lecture-attachment-type-text'
    id="lecture-attachment-23038655">
    <div class="attachment-data"></div>
  </div>
    

<div class="lecture-text-container">
<p><p>In this section you learned that:</p><ul><li>A&#xA0;list comprehension is an expression that creates a list by iterating over another container.&#xA0;</li><li>A&#xA0;<strong>basic&#xA0;</strong>list comprehension:</li></ul><pre class="ql-syntax" spellcheck="false">[i*2 for i in [1, 5, 10]]
</pre><ul><li>Output:&#xA0;<code>[2, 10, 20]</code></li><li>List comprehension with&#xA0;<strong>if</strong>condition:</li></ul><pre class="ql-syntax" spellcheck="false">[i*2 for i in [1, -2, 10] if i&gt;0]
</pre><ul><li>Output:&#xA0;<code>[2, 20]</code></li><li>List comprehension with an&#xA0;<strong>ifandelse</strong>condition:</li></ul><pre class="ql-syntax" spellcheck="false">[i*2 if i&gt;0 else 0 for i in [1, -2, 10]]
</pre><ul><li>Output:&#xA0;<code>[2, 0, 20]</code></li></ul><p><br></p>
</div>
