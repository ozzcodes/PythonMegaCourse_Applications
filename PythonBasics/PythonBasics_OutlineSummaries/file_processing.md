<h2>&nbsp;Summary: File Processing</h2>

  <!-- Attachment Blocks -->

  <div
    class='lecture-attachment lecture-attachment-type-text'
    id="lecture-attachment-23038993"
  >
    <div class="attachment-data"></div>
    

<div class="lecture-text-container">
<p><p>In this section you learned that:</p><ul><li>You can&#xA0;<strong>read</strong>an existing file with Python:</li></ul><pre class="ql-syntax" spellcheck="false">with open(&quot;file.txt&quot;) as file:
    content = file.read()
</pre><ul><li>You can&#xA0;<strong>create</strong>a new file with Python and&#xA0;<strong>write</strong>some text on it:</li></ul><pre class="ql-syntax" spellcheck="false">with open(&quot;file.txt&quot;, &quot;w&quot;) as file:
    content = file.write(&quot;Sample text&quot;)
</pre><ul><li>You can&#xA0;<strong>append</strong>text to an existing file without overwriting it:</li></ul><pre class="ql-syntax" spellcheck="false">with open(&quot;file.txt&quot;, &quot;a&quot;) as file:
    content = file.write(&quot;More sample text&quot;)
</pre><ul><li>You can both&#xA0;<strong>append and read</strong>a file with:</li></ul><pre class="ql-syntax" spellcheck="false">with open(&quot;file.txt&quot;, &quot;a+&quot;) as file:
    content = file.write(&quot;Even more sample text&quot;)
    file.seek(0)
    content = file.read()
</pre><p><br></p>
</div>

    
</div>