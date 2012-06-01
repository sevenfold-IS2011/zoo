<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
		<h3>Animali:</h3>
		<table class = "standard">
			<tr>
				<th colspan="2">Azioni</th>
				<th>Area</th>
				<th>Nome</th>
				<th>Eta'</th>
				<th>Sesso</th>
				<th>Immagine</th>
			</tr>
			<xsl:for-each select="zoo:area">
				<xsl:for-each select="zoo:animale">
					<tr>
						<td><button>Modifica</button></td>
						<td><button>Elimina</button></td>
						<td><xsl:value-of select="../@nome"/></td>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td><a href="#"><xsl:value-of select="zoo:img" /></a></td>
					</tr>
				</xsl:for-each>
			</xsl:for-each>
		</table>
	</xsl:template>
</xsl:stylesheet>

