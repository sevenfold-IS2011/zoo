<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
		<h3>Animali:</h3>
		<table class = "standard" summary="tabella contenente la lista degli animali e tutti i loro attributi">
			<tr class="title">
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
							<a class="button" onclick='edit(this);return false'>
								<xsl:attribute name="animal_name">
									<xsl:value-of select="zoo:nome"/>
								</xsl:attribute> 
								<xsl:attribute name="href">
									modifica_animale.cgi?noscript=true&amp;name=<xsl:value-of select="zoo:nome"/>
								</xsl:attribute>
								Modifica
							</a>
						</td>
						<td>
							<a href="reply.cgi?.." class="button" onclick='destroy(this);return false'><xsl:attribute name="href">
								reply.cgi?noscript=true&amp;watDo=animals&amp;action=destroy&amp;name=<xsl:value-of select="zoo:nome"/>
								</xsl:attribute>
								<xsl:attribute name="animal_name">
									<xsl:value-of select="zoo:nome"/>
								</xsl:attribute>
								Elimina
							</a>
						</td>
						<td><xsl:value-of select="../@nome"/></td>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td>
							<a class="button" href ="#" onclick='show_image(this);return false'>
								<xsl:attribute name="image_path">
									<xsl:value-of select="zoo:img"/>
								</xsl:attribute>
								Visualizza
							</a>
						</td>
					</tr>
				</xsl:for-each>
			</xsl:for-each>
		</table>
	</xsl:template>
</xsl:stylesheet>

