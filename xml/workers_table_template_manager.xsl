<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:workers">

			<h4>Di seguito è riportata la lista del personale dello zoo con i relativi dati modificabili (solo per Manager).</h4>

			<table class="standard">
				<tr class="title">
					<td>Nome</td>
					<td>Età</td>
					<td>Sesso</td>
					<td>Tipo</td>
					<td>Stipendio</td>
				</tr>
				<xsl:for-each select="zoo:impiegato">
					<tr>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td>Impiegato</td>
						<td><xsl:value-of select="zoo:stipendio"/></td>
						<td class="button">
							<button onclick='edit(this)'>
								<xsl:attribute name="username">
									<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								Modifica
							</button>
						</td>
						<td class="button">
							<button onclick='destroy(this)'>
								<xsl:attribute name="username">
									<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								Rimuovi
							</button>
						</td>
					</tr>
				</xsl:for-each>
				<xsl:for-each select="zoo:manager">
					<tr>
						<td><xsl:value-of select="zoo:nome"/></td>
						<td><xsl:value-of select="zoo:eta"/></td>
						<td><xsl:value-of select="zoo:sesso"/></td>
						<td>Manager</td>
						<td><xsl:value-of select="zoo:stipendio"/></td>
						<td class="button">
							<button onclick='edit(this)'>
								<xsl:attribute name="username">
									<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								Modifica
							</button>
						</td>
						<td class="button">
							<button onclick='destroy(this)'>
								<xsl:attribute name="username">
									<xsl:value-of select="zoo:username"/>
								</xsl:attribute>
								Rimuovi
							</button>
						</td>
					</tr>
				</xsl:for-each>
			</table>



















	</xsl:template>
</xsl:stylesheet>

