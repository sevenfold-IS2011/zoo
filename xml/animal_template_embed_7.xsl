<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
		<h3>Animals descriptions:</h3>
			<xsl:for-each select="zoo:area">
			<xsl:if test="@id=7">
				<h4><xsl:value-of select="./@nome"/> list:</h4>
					<xsl:for-each select="zoo:animale">
					<table class="animal">
  				<tr>
						<td>Name</td>
						<td><xsl:value-of select="zoo:nome"/></td>
					</tr>
					<tr>
						<td>Gender</td>
						<td><xsl:value-of select="zoo:sesso"/></td>
					</tr>
					<tr>
						<td>Age</td>
						<td><xsl:value-of select="zoo:età"/></td>
					</tr>
					<tr>
						<td></td>
						<td>
							<img>
      					<xsl:attribute name="src">
      						<xsl:value-of select="zoo:img" />
      					</xsl:attribute>
    					</img>
    				</td>
					</tr>
				</table>
					</xsl:for-each>
			</xsl:if>
			</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>

