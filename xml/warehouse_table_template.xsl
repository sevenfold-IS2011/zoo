<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">


			<h4>Di seguito è riportata la lista delle scorte presenti nel magazzino.</h4>
			<table class="standard">
				<tr class="title">
					<td>Nome</td>
					<td>Area</td>
					<td>Quantità</td>
					<td colspan="3">Aggiungi/Rimuovi</td>
					<td>Elimina</td>
				</tr>
				<xsl:for-each select="zoo:cibo">
					<tr>
						<td><xsl:value-of select="@nome"/></td>
						<td>
							<xsl:for-each select="zoo:area">
								<a>
									<xsl:attribute name="href">area.cgi?id=<xsl:value-of select="."/></xsl:attribute>
								<xsl:value-of select="."/>
								</a>&#160;
							</xsl:for-each>
						</td>
						<td><xsl:value-of select="@quantita"/></td>
						<td class="button">
							<input placeholder="Quantità">
								<xsl:attribute name="id">
									<xsl:value-of select="@id"/>
								</xsl:attribute>
							</input>
						</td>
						<td class="button">
							<button onclick='add(this)'>
								<xsl:attribute name="id">
									<xsl:value-of select="@id"/>
								</xsl:attribute>
								Aggiungi
							</button>
						</td>
						<td class="button">
							<button onclick='remove(this)'>
								<xsl:attribute name="id">
									<xsl:value-of select="@id"/>
								</xsl:attribute>
								Rimuovi
							</button>
						</td>
						<td class="button">
							<button onclick='destroy(this)'>
								<xsl:attribute name="id">
									<xsl:value-of select="@id"/>
								</xsl:attribute>
								Elimina
							</button>
						</td>
					</tr>
				</xsl:for-each>
			</table>
	</xsl:template>
</xsl:stylesheet>

