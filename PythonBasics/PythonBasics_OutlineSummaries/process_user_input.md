<h2>
    &nbsp;
    Summary: Processing User Input
</h2>
<div class="attachment-data"></div>
   
<div class="lecture-text-container">
<p><p>In this section you learned that:</p><ul><li>A&#xA0;Python program can get&#xA0;<strong>user input</strong>via the&#xA0;<code>input</code>&#xA0;function:</li><li>The&#xA0;<strong>inputfunction</strong>halts the execution of the program and gets text input from the user<strong>:</strong></li></ul><pre class="ql-syntax" spellcheck="false">name = input(&quot;Enter your name: &quot;)
</pre><ul><li>The input function converts any&#xA0;<strong>input to a string</strong>, but you can convert it back to int or float:</li></ul><pre class="ql-syntax" spellcheck="false">experience_months = input(&quot;Enter your experience in months: &quot;)
experience_years = int(experience_months) / 12)
</pre><ul><li>You can&#xA0;<strong>format strings</strong>with (works both on Python 2 and 3):</li></ul><pre class="ql-syntax" spellcheck="false">name = &quot;Sim&quot;
experience_years = 1.5
print(&quot;Hi %s, you have %s years of experience.&quot; % (name, experience_years))
</pre><p>Output:&#xA0;<code>Hi Sim, you have 1.5 years of experience.</code></p><ul><li>You can also&#xA0;<strong>format strings</strong>with (Python 3 only):</li></ul><pre class="ql-syntax" spellcheck="false">name = &quot;Sim&quot;
experience_years = 1.5
print(&quot;Hi {}, you have {} years of experience&quot;.format(name, experience_years))
</pre><p>Output:&#xA0;<code>Hi Sim, you have 1.5 years of experience.</code></p>
</div>
