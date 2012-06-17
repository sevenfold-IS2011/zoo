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
							<form action="modifica_animale.cgi" method="get">
								<input type="hidden" name="name">
									<xsl:attribute name="value">
										<xsl:value-of select="zoo:nome"/>
									</xsl:attribute>
								</input>
								<input type ="submit" value="Modifica" />
							</form>
						</td>
						<td>      
							<form action="reply.cgi" method="get">
								<input type="hidden" name="name">
									<xsl:attribute name="value">
										<xsl:value-of select="zoo:nome"/>
									</xsl:attribute>
								</input>
								<input type="hidden" name="watDo" value="animals" /> 
								<input type="hidden" name="action" value="destroy" /> 
								<input type="hidden" name="noscript" value="true" /> 
								<input type ="submit" value="Elimina" />
							</form>
						</td>
						<td><xsl:value-of select="../@nome"/></td>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td>
							<button onclick='show_image(this)'>
								Visualizza
							</button>
						</td>
						<td class="hidden"><xsl:value-of select="zoo:img"/></td>
					</tr>
				</xsl:for-each>
			</xsl:for-each>
		</table>
	</xsl:template>
</xsl:stylesheet>

