<!-- Lecture Content -->
<div class="course-mainbar lecture-content">
    <!-- Meta tag for tracking lecture progress -->
    <meta id="lecture-completion-data" data-last-lecture-id="11418235"
          data-last-lecture-url="/courses/100908/lectures/11418235" data-is-completed="false"
          data-can-access-lecture="true" data-compliance-enabled="false" data-valid-for-completion="true"/>
    <h2 id="lecture_heading" class="section-title" data-lecture-id="11418235" data-next-lecture-id="11417935"
        data-lecture-url="/courses/100908/lectures/11418235" data-next-lecture-url="/courses/100908/lectures/11417935"
        data-previous-lecture-url="/courses/100908/lectures/11417920" data-previous-lecture-id="11417920">
        <i class="fa fa-file-text"></i>
        &nbsp;
        Summary: Positive/Negative Indexes, Slicing
    </h2>


<pre class="ql-syntax" spellcheck="false">[&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
  -7     -6     -5     -4     -3     -2     -1
</pre>
<ul>
<li>In a list, the&#xA0;<strong>2nd</strong>,&#xA0;<strong>3rd</strong>, and&#xA0;<strong>4th</strong>items
    can be accessed with:
</li>
</ul>
<pre class="ql-syntax" spellcheck="false">days = [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
    days[1:4]
    Output: [&apos;Tue&apos;, &apos;Wed&apos;, &apos;Thu&apos;]
</pre>
            <ul>
                <li><strong>First three items of a list</strong>:</li>
            </ul>
            <pre class="ql-syntax" spellcheck="false">days = [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
days[:3]
Output:[&apos;Mon&apos;, &apos;Tue&apos;, &apos;Wed&apos;]&#xA0;
</pre>
            <ul>
                <li><strong>Last three items of a list</strong>:</li>
            </ul>
            <pre class="ql-syntax" spellcheck="false">days = [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
days[-3:]
Output: [&apos;Fri&apos;, &apos;Sat&apos;, &apos;Sun&apos;]
</pre>
            <ul>
                <li><strong>Everything but the last</strong>:</li>
            </ul>
            <pre class="ql-syntax" spellcheck="false">days = [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
days[:-1]&#xA0;
Output:&#xA0;[&apos;Mon&apos;, &apos;Tue&apos;, &apos;Wed&apos;, &apos;Thu&apos;, &apos;Fri&apos;, &apos;Sat&apos;]&#xA0;
</pre>
            <ul>
                <li><strong>Everything but the last two</strong>:</li>
            </ul>
            <pre class="ql-syntax" spellcheck="false">days = [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
days[:-2]&#xA0;
Output:&#xA0;[&apos;Mon&apos;, &apos;Tue&apos;, &apos;Wed&apos;, &apos;Thu&apos;, &apos;Fri&apos;]&#xA0;
</pre>
            <ul>
                <li>A single in a&#xA0;<strong>dictionary</strong>can be accessed using its key:</li>
            </ul>
            <pre class="ql-syntax" spellcheck="false">phone_numbers = {&quot;John Smith&quot;:&quot;+37682929928&quot;,&quot;Marry Simpons&quot;:&quot;+423998200919&quot;}
phone_numbers[&quot;Marry Simpsons&quot;]
Output:&#xA0;&apos;+423998200919&apos;
</pre>
            <p><br></p>
        </div>


