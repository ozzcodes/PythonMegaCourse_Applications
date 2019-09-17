<h2> Summary: Functions and Conditionals</h2>

  <!-- Attachment Blocks -->
    
<div class="attachment-data"></div>
<div class="lecture-text-container">
<p><p>In this section you learned to:</p><ul><li>To define a&#xA0;<strong>function</strong>:</li></ul><pre class="ql-syntax" spellcheck="false">def cube_volume(a):
    return a *&#xA0;a *&#xA0;a
</pre><ul><li>To write a&#xA0;<strong>conditional&#xA0;</strong>block:</li></ul><pre class="ql-syntax" spellcheck="false">message = &quot;hello there&quot;

if &quot;hello&quot; in message:
    print(&quot;hi&quot;)
else:
    print(&quot;I&#xA0;don&apos;t understand&quot;)
</pre><ul><li>To write a conditional block of&#xA0;<strong>multiple conditions</strong>:</li></ul><pre class="ql-syntax" spellcheck="false">message = &quot;hello there&quot;

if &quot;hello&quot; in message:
    print(&quot;hi&quot;)
elif &quot;hi&quot; in message:
    print(&quot;hi&quot;)
elif &quot;hey&quot; in message:
    print(&quot;hi&quot;)
else:
    print(&quot;I don&apos;t understand&quot;)
</pre><ul><li>To check if a value is of a certain&#xA0;<strong>type</strong>with:</li></ul><pre class="ql-syntax" spellcheck="false">isinstance(&quot;abc&quot;, str)
isinstance([1, 2, 3], list)
</pre><p>or</p><pre class="ql-syntax" spellcheck="false">type(&quot;abc&quot;) == str
type([1, 2, 3]) == lst
</pre><p><br></p>
</div>
