<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">


			<h4>Scorte:</h4>
			<table class="standard">
				<tr class="title">
					<td>id</td>
					<td>nome</td>
					<td>area</td>
					<td>quantità</td>
				</tr>
				<xsl:for-each select="zoo:cibo">
					<tr>
						<td><xsl:value-of select="@id"/></td>
						<td><xsl:value-of select="@nome"/></td>
						<td><xsl:value-of select="@area"/></td>
						<td><xsl:value-of select="zoo:quantita"/></td>
						<td class="button">
							<button onclick='edit(this)'>
								<xsl:attribute name="username">
									<xsl:value-of select="@id"/>
								</xsl:attribute>
								Modifica
							</button>
						</td>
					</tr>
				</xsl:for-each>
			</table>

	</xsl:template>
</xsl:stylesheet>

