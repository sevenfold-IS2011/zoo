<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:workers">

			<h4>Impiegati:</h4>
			<table class="standard">
				<tr class="title">
					<td>Nome</td>
					<td>Età</td>
					<td>Sesso</td>
				</tr>
				<xsl:for-each select="zoo:employee">
					<tr>
						<td><xsl:value-of select="zoo:name"/></td>
						<td><xsl:value-of select="zoo:age"/></td>
						<td><xsl:value-of select="zoo:gender"/></td>
					</tr>
				</xsl:for-each>
			</table>

			<h4>Manager:</h4>
			<table class="standard">
				<tr class="title">
					<td>Nome</td>
					<td>Età</td>
					<td>Sesso</td>
					<td>Salario</td>
				</tr>
				<xsl:for-each select="zoo:manager">
					<tr>
						<td><xsl:value-of select="zoo:name"/></td>
						<td><xsl:value-of select="zoo:age"/></td>
						<td><xsl:value-of select="zoo:gender"/></td>
						<td><xsl:value-of select="zoo:salary"/></td>
					</tr>
				</xsl:for-each>
			</table>



	</xsl:template>
</xsl:stylesheet>

