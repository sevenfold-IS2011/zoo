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
						<td>
							<button onclick='edit(this)'>
								<xsl:attribute name="animal_name">
									<xsl:value-of select="zoo:nome"/>
								</xsl:attribute>
								Modifica
							</button>
						</td>
						<td>
							<button onclick='destroy(this)'>
								<xsl:attribute name="animal_name">
									<xsl:value-of select="zoo:nome"/>
								</xsl:attribute>
								Elimina
							</button>
						</td>
						<td><xsl:value-of select="../@nome"/></td>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td>
							<button onclick='show_image(this)'>
								<xsl:attribute name="image_path">
									<xsl:value-of select="zoo:img"/>
								</xsl:attribute>
								Visualizza
							</button>
						</td>
					</tr>
				</xsl:for-each>
			</xsl:for-each>
		</table>
	</xsl:template>
</xsl:stylesheet>

