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
					<td colspan="4">Modifica</td>
				</tr>
				<xsl:for-each select="zoo:cibo">
					<tr>
						<td><xsl:value-of select="@nome"/></td>
						<td><xsl:value-of select="@area"/></td>
						<td><xsl:value-of select="zoo:quantita"/></td>
						<td class="button">
							<input>
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

