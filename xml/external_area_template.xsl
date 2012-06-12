<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
		<div id="content">
			<h3>Il nostro parco</h3>
			<p>All&apos;interno dello spazio dedicato ai visitatori &#232; possibile visitare il percorso safari o a piedi. Si possono trovare zone di ristoro e divertimento per i pi&#249; piccoli.</p>
			<h3>Mappa</h3>
			<div class="figure">
				<img src="../images/map.png" />
				<p>La mappa del parco Monkey Island</p>
			</div>
			<h3>Aree</h3>
			<xsl:for-each select="zoo:area">

				<h4>Area <xsl:value-of select="./@nome"/></h4>

			</xsl:for-each>
		</div>
	</xsl:template>
</xsl:stylesheet>

