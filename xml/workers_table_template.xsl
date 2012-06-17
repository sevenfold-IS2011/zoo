<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:workers">

		<h4>Di seguito è riportata la lista del personale dello zoo.</h4>
			<table class="standard" summary="tabella contenete la ista del personale dello zoo">
				<tr class="title">
					<td>Nome</td>
					<td>Età</td>
					<td>Sesso</td>
					<td>Tipo</td>
				</tr>
				<xsl:for-each select="zoo:impiegato">
					<tr>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td>Impiegato</td>
					</tr>
				</xsl:for-each>
				<xsl:for-each select="zoo:manager">
					<tr>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td>Manager</td>
					</tr>
				</xsl:for-each>
			</table>

	</xsl:template>
</xsl:stylesheet>

