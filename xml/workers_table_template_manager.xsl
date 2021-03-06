<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:workers">

			<h4>Di seguito è riportata la lista del personale dello zoo con i relativi dati modificabili (solo per Manager).</h4>
			<table class="standard" summary="tabella contenete la ista del personale dello zoo">
				<tr class="title">
					<th>Nome</th>
					<th>Età</th>
					<th>Sesso</th>
					<th>Tipo</th>
					<th colspan="2">Azioni</th>
				</tr>
				<xsl:for-each select="zoo:impiegato">
					<tr>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td>Impiegato</td>
						<td class="button">
							<a class="button">
								<xsl:attribute name="username">
									<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								<xsl:attribute name="href">
									modifica_utente.cgi?user=<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								Modifica
							</a>
						</td>
						<td class="button">
							<a class="button" onclick='destroy(this);return false'>
								<xsl:attribute name="username">
									<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								<xsl:attribute name="href">
									reply.cgi?noscript=true&amp;watDo=users&amp;action=destroy&amp;username=<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								Rimuovi
							</a>
						</td>
					</tr>
				</xsl:for-each>
				<xsl:for-each select="zoo:manager">
					<tr>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td>Manager</td>
						<td class="button">
							<a class="button" onclick='edit(this);return false'>
								<xsl:attribute name="username">
									<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								<xsl:attribute name="href">
									modifica_utente.cgi?user=<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								Modifica
							</a>
						</td>
						<td class="button">
							<a class="button" onclick='destroy(this);return false'>
								<xsl:attribute name="username">
									<xsl:value-of select="zoo:username"/>
								</xsl:attribute> 
								<xsl:attribute name="href">
									reply.cgi?noscript=true&amp;watDo=users&amp;action=destroy&amp;username=<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								Rimuovi
							</a>
						</td>
					</tr>
				</xsl:for-each>
			</table>

	</xsl:template>
</xsl:stylesheet>

