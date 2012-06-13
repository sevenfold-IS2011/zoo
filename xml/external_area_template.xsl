<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
		<div id="content">
			<h3>Il nostro parco: </h3>
			<p>All&apos;interno dello spazio dedicato ai visitatori &#232; possibile visitare il percorso safari o a piedi. Si possono trovare zone di ristoro e divertimento per i pi&#249; piccoli.</p>
			<h3>Aree: </h3>
			<table class="striped" summary="tabella contenente la lista delle aree presenti nello zoo">
				<xsl:for-each select="zoo:area">
					<tr>
						<td>
							<a>
								<xsl:attribute name="href">
									area.cgi?id=<xsl:value-of select="./@id" />
								</xsl:attribute>  
								<span class="stripe">Area <xsl:value-of select="./@nome"/></span>
							</a>
						</td>
					</tr>
				</xsl:for-each>
			</table>
			<h3>Mappa: </h3>
			<div class="figure">
				<img src="../images/map.png" />
				<p>La mappa del parco Monkey Island</p>
			</div>
		</div>
	</xsl:template>
</xsl:stylesheet>

