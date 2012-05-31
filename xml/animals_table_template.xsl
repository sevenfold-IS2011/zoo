<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
		<h3>Animali:</h3>
		<table>
			<th>
				<td>Area</td>
				<td>Nome</td>
				<td>Et&grave;</td>
				<td>Sesso</td>
				<td>Immagine</td>
			</th>
			<xsl:for-each select="zoo:area">
				<xsl:for-each select="zoo:animale">
					<tr>
						<td><xsl:value-of select="./@nome"/></td>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td><a href="#"><xsl:value-of select="zoo:img" /></a></td>
					</tr>
				</xsl:for-each>
			</xsl:for-each>
		<table>
	</xsl:template>
</xsl:stylesheet>

