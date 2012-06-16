<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:zoo">

		<h4>Di seguito è riportata la lista delle scorte presenti nel magazzino.</h4>
		<table class="standard" summary="tabella contenente la lista lista delle scorte presenti nel magazzino">
			<tr class="title">
				<th>Nome</th>
				<th>Area</th>
				<th>Quantità</th>
				<th colspan="2">Modifica/Rimuovi</th>
			</tr>
			<xsl:for-each select="zoo:cibo">
				<xsl:sort select="@id"/>
				<tr>
					<td><xsl:value-of select="@nome"/></td>
					<td>
						<xsl:for-each select="zoo:area">
							<a><xsl:attribute name="href">area.cgi?id=<xsl:value-of select="."/></xsl:attribute><xsl:value-of select="."/>[_]</a><!-- Non mandare a capo -->
						</xsl:for-each>
					</td>
					<td><xsl:value-of select="@quantita"/></td>
					<td class="button">
						<a class="button" onclick="destroy(this)">
							<xsl:attribute name="href">modifica_magazzino.cgi?id=<xsl:value-of select="@id" /> 
						</xsl:attribute>
						Modifica
					</a>
				</td>
				<td class="button">
					<a class="button" onclick="destroy(this)">
						<xsl:attribute name="href">reply.cgi?noscript=true&amp;watDo=warehouse&amp;action=destroy&amp;cibo=<xsl:value-of select="@id" /> 
					</xsl:attribute>
					Rimuovi
				</a>
			</td>
		</tr>
	</xsl:for-each>
</table>
<h4>Aggiornamento magazzino</h4>
<form action = "reply.cgi" method="get">
	<fieldset>
		<input type="hidden" name="watDo" value="warehouse" />
		<input type="hidden" name="noscript" value="true" />
		<select name="cibo">
			<xsl:for-each select="zoo:cibo">
				<xsl:sort select="@id"/>
				<option>
					<xsl:attribute name="value">
						<xsl:value-of select="@id" /> 
					</xsl:attribute>
					<xsl:value-of select="@nome" />
				</option>
			</xsl:for-each>
		</select>
		<input type="text" name="amount" />
		<input type="submit" name="action" value="Aggiungi" />
		<input type="submit" name="action" value ="Rimuovi" />
	</fieldset>
</form>
</xsl:template>
</xsl:stylesheet>

