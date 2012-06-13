<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">

		<h4>Di seguito è riportata la lista delle aree presenti nello zoo.</h4>
		<table class = "standard" summary="La tabella contiene un listato delle aree dello zoo con le loro caratteristiche registrate. &#200; possibile inoltre eliminare o modificare dati seguendo i link nell'ultima parte di ogni riga.">
			<tr class="title">
				<th scope="col">Area</th>
				<th scope="col">Id</th>
				<th scope="col">Posizione</th>
				<th scope="col">Cibo giornaliero</th>
				<th scope="col" colspan="2">Azioni</th>
			</tr>
			<xsl:for-each select="zoo:area">
				<tr>
					<td scope="row"><xsl:value-of select="@nome"/></td>
					<td><xsl:value-of select="@id"/></td>
					<td><xsl:value-of select="@posizione"/></td>
					<td><xsl:value-of select="@cibo_giornaliero"/></td>
					<td class="button">
						<a class="button" onclick='edit(this)'>
							<xsl:attribute name="id">
								<xsl:value-of select="@id"/>
							</xsl:attribute>
							<xsl:attribute name="href">
								modifica_area.cgi?id=<xsl:value-of select="@id" />
							</xsl:attribute>
							Modifica
						</a>
					</td>
					<td class ="button">
						<a class="button" onclick='destroy(this)'>
							<xsl:attribute name="id">
								<xsl:value-of select="@id"/>
							</xsl:attribute>
							<xsl:attribute name="href">
								reply.cgi?watDo=areas&amp;action=destroy&amp;noscript=true&amp;id=<xsl:value-of select="@id" />
							</xsl:attribute>
							Elimina
						</a>
					</td>
					 
				</tr>
			</xsl:for-each>
		</table>
	</xsl:template>
</xsl:stylesheet>

