<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
		<div id="content">
			<h3>I nostri animali: </h3>
			<h3>Aree: </h3>
			<xsl:for-each select="zoo:area">
				<h4><xsl:value-of select="./@nome"/>: </h4>
				<table class="striped">
					<xsl:for-each select="zoo:animale">
						<tr>
							<td>
								<a>
									<xsl:attribute name="href">
										animali.cgi?name=<xsl:value-of select="zoo:nome" />
									</xsl:attribute>  
									<span class="stripe"><xsl:value-of select="zoo:nome"/></span>
								</a>
							</td>
						</tr> 
					</xsl:for-each>
				</table> 
			</xsl:for-each>
		</div>
	</xsl:template>
</xsl:stylesheet>

