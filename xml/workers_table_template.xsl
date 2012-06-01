<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:workers">


<!-- -->
	<html>
		<head>
		<link rel="stylesheet" type="text/css" href="../css/master.css" />
	</head>
		<body>
<!-- -->

		<form action="../cgi-bin/_gestione_utenti.cgi" method="post" accept-charset="utf-8">
			<h4>Impiegati:</h4>
			<table class="standard">
				<tr>
					<td>Username:</td>
					<td>Nome</td>
					<td>Sesso</td>
					<td>Eta</td>
				</tr>
				<xsl:for-each select="zoo:employee">
					<tr>
						<td><xsl:value-of select="zoo:username"/></td>
						<td><xsl:value-of select="zoo:name"/></td>
						<td><xsl:value-of select="zoo:gender"/></td>
						<td><xsl:value-of select="zoo:age"/></td>
						<td>
							<input type="submit" name="Modifica" value="Modifica">
								<xsl:attribute name="id">
									 <xsl:value-of select="zoo:username"/>
								</xsl:attribute>
							</input>
						</td>
						<td>
							<input type="submit" name="Rimuovi" value="Rimuovi">
								<xsl:attribute name="id">
								 <xsl:value-of select="zoo:username"/>
								</xsl:attribute>
							</input>
						</td>
					</tr>
				</xsl:for-each>
			</table>

			<h4>Manager:</h4>
			<table class="standard">
				<tr>
					<td>Username:</td>
					<td>Nome</td>
					<td>Sesso</td>
					<td>Eta</td>
					<td>Salario</td>
				</tr>
				<xsl:for-each select="zoo:manager">
					<tr>
						<td><xsl:value-of select="zoo:username"/></td>
						<td><xsl:value-of select="zoo:name"/></td>
						<td><xsl:value-of select="zoo:gender"/></td>
						<td><xsl:value-of select="zoo:age"/></td>
						<td><xsl:value-of select="zoo:salary"/></td>
						<td>
							<input type="submit" name="Modifica" value="Modifica">
								<xsl:attribute name="id">
								 <xsl:value-of select="zoo:username"/>
								</xsl:attribute>
							</input>
						</td>
						<td>
							<input type="submit" name="Rimuovi" value="Rimuovi">
								<xsl:attribute name="id">
								 <xsl:value-of select="zoo:username"/>
								</xsl:attribute>
							</input>
						</td>
					</tr>
				</xsl:for-each>
			</table>
		</form>


<!-- -->
		</body>
	</html>
<!-- -->


	</xsl:template>
</xsl:stylesheet>

