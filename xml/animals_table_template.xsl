<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">
		<h4>Di seguito è riportata la lista degli animali e delle loro caratteristiche:</h4>
		<table class = "standard" summary="tabella contenente la lista degli animali e tutti i loro attributi">
			<tr class="title">
				<th scope="col">Nome</th>
				<th scope="col">Eta'</th>
				<th scope="col">Sesso</th>
				<th scope="col">Area</th>
				<th scope="col">Immagine</th>
				<th scope="col" colspan="2">Azioni</th>
			</tr>
			<xsl:for-each select="zoo:area">
				<xsl:for-each select="zoo:animale">
					<tr>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td scope="row"><a><xsl:attribute name="href">area.cgi?id=<xsl:value-of select="../@id"/></xsl:attribute><xsl:value-of select="../@nome"/></a></td>
						<td>
							<a class="button" href ="#" onclick='show_image(this);return false'>
								<xsl:attribute name="image_path">
									<xsl:value-of select="zoo:img"/>
								</xsl:attribute>
								Visualizza
							</a>
						</td>
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
					</tr>
				</xsl:for-each>
			</xsl:for-each>
		</table>
	</xsl:template>
</xsl:stylesheet>

