Title: Using Zend to retrive wikipedia api content
Date: 2012-05-22 08:15
Author: Andrew Elkins
Category: Programming
Slug: using-zend-to-retrive-wikipedia-api-content
Status: published

> function getWikipediaContent( \$wikiUrl )
>
> {
>
> // initialize HTTP client  
> \$client = new Zend\_Http\_Client();  
> // Set it for wikipedia  
> \$client-&gt;setUri( \$wikiUrl );  
> // Set url params for get request  
> \$client-&gt;setParameterGet('action','query');  
> \$client-&gt;setParameterGet('prop','revisions');  
> \$client-&gt;setParameterGet('rvprop','content');  
> \$client-&gt;setParameterGet('format','xml');  
> \$client-&gt;setParameterGet('titles', \$urlSlug);  
> // Get the wiki page via a get request  
> \$result = \$client-&gt;request('GET');
>
> // Make sure actual data was returned. If not, return false  
> if( \$result-&gt;isError() )  
> {  
> return false;  
> }
>
> // Put response body in to variable  
> \$body = \$result-&gt;getBody();
>
> // Transform string in to xml feed so it can be parsed.  
> \$wikiXml = new SimpleXMLElement( \$body );  
> // Get body and transform back to string.  
> return (string)
> \$wikiXml-&gt;query-&gt;pages-&gt;page-&gt;revisions-&gt;rev;
>
> }
